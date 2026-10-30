"""
Sincroniza labels e bloco de metadados Project/PSM no corpo das issues,
a partir do que já está documentado em cada issue e em gestao-psm/calendario-progresso.csv.

Campos do GitHub Projects V2 exigem escopo read:project/project (não disponível
neste token). Este script atualiza o que a API com escopo repo permite:
corpo da issue + labels.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = "FCTE-Qualidade-de-Software-1"
REPO = "2026-2_T01_BETTY_SNYDER"
CSV_PATH = ROOT / "gestao-psm" / "calendario-progresso.csv"
COST_PER_HOUR = 35.0
MARKER_START = "<!-- PSM-PROJECT-FIELDS:START -->"
MARKER_END = "<!-- PSM-PROJECT-FIELDS:END -->"
DRY_RUN = False


def get_token() -> str:
    p = subprocess.Popen(
        ["git", "credential", "fill"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(ROOT),
    )
    out, _ = p.communicate("protocol=https\nhost=github.com\n\n")
    for line in out.splitlines():
        if line.startswith("password="):
            return line[9:]
    raise RuntimeError("Token GitHub não encontrado no credential helper")


def api(method: str, path: str, token: str, payload=None):
    url = f"https://api.github.com{path}"
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "betty-psm-sync",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read().decode("utf-8")
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {path} -> {e.code}: {body[:500]}") from e


def list_issues(token: str):
    issues = []
    page = 1
    while True:
        batch = api(
            "GET",
            f"/repos/{OWNER}/{REPO}/issues?state=all&per_page=100&page={page}",
            token,
        )
        batch = [i for i in batch if "pull_request" not in i]
        if not batch:
            break
        issues.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return issues


def dig(body: str, *keys: str) -> str:
    body = body or ""
    for k in keys:
        m = re.search(rf"\*\*{re.escape(k)}\*\*:\s*`?([^`\n]+)`?", body, re.I)
        if m:
            return m.group(1).strip()
    return ""


def load_csv():
    rows = {}
    with CSV_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows[row["tarefa_id"]] = row
    return rows


def infer_activity_id(issue: dict, body: str) -> str:
    aid = dig(body, "ID da atividade")
    if aid:
        return aid
    title = issue.get("title") or ""
    m = re.search(r"\b([REP]\d[\w-]*|[A-Z]\d+-[A-Z0-9-]+)\b", title)
    if m:
        return m.group(1)
    m = re.search(r"\[TASK\]\s*([A-Z0-9-]+)", title)
    return m.group(1) if m else ""


def map_status_label(csv_status: str, concluida_no_prazo: str, gh_state: str) -> str:
    st = (csv_status or "").lower()
    if gh_state == "closed" or st == "concluida":
        if (concluida_no_prazo or "").lower() == "sim":
            return "status:on-time"
        if (concluida_no_prazo or "").lower() == "nao":
            return "status:late"
        return "status:on-time"
    if st == "parcial":
        return "status:partial"
    return "status:pending"


def project_status(csv_status: str, gh_state: str) -> str:
    st = (csv_status or "").lower()
    if gh_state == "closed" or st == "concluida":
        return "Done"
    if st == "parcial":
        return "In Progress"
    return "Todo"


def progress_pct(status: str) -> str:
    return {"Done": "100", "In Progress": "50"}.get(status, "0")


def psm_label_from_id(aid: str, title: str) -> str:
    t = f"{aid} {title}".lower()
    if any(x in t for x in ["recurso", "custo", "hora", "psm de recursos"]):
        return "psm:resources-cost"
    if any(x in t for x in ["desempenho", "defeito", "processo"]):
        return "psm:process-performance"
    if any(x in t for x in ["calend", "progresso", "prazo", "milestone", "issue"]):
        return "psm:schedule-progress"
    # default: atividades de projeto acompanham calendário/progresso
    return "psm:schedule-progress"


def type_label_from_existing(labels: list[str], title: str) -> str:
    for name in labels:
        if name.startswith("type:"):
            return name
    if "[DOC]" in title or "ata" in title.lower() or "texto" in title.lower():
        return "type:documentation"
    if "[MEAS]" in title:
        return "type:measurement"
    if "[IMPROVE]" in title:
        return "type:improvement"
    return "type:execution"


def priority_label(labels: list[str]) -> str:
    for name in labels:
        if name.startswith("priority:"):
            return name
    return "priority:medium"


def env_label(labels: list[str]) -> str:
    for name in labels:
        if name.startswith("environment:"):
            return name
    return "environment:cross-platform"


def strip_old_block(body: str) -> str:
    body = body or ""
    if MARKER_START in body and MARKER_END in body:
        return re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END) + r"\s*",
            "",
            body,
            flags=re.S,
        ).rstrip()
    # remove bloco legado sem marcadores
    body = re.sub(
        r"\n## Campos do Project \(PSM\).*?(?=\n## |\Z)",
        "",
        body,
        flags=re.S,
    )
    return body.rstrip()


def build_block(meta: dict) -> str:
    lines = [
        MARKER_START,
        "## Campos do Project (PSM)",
        "",
        "Preencha estes valores no quadro **Anki Quality Assessment: PSM/CID**.",
        "Custo estimado: C = H x 35 (R$ 35,00/h).",
        "",
        f"- **Status:** `{meta['Status']}`",
        f"- **Priority:** `{meta['Priority']}`",
        f"- **Quality Attribute:** `{meta['Quality Attribute']}`",
        f"- **Activity Type:** `{meta['Activity Type']}`",
        f"- **Platform:** `{meta['Platform']}`",
        f"- **Planned Effort (h):** `{meta['Planned Effort (h)']}`",
        f"- **Actual Effort (h):** `{meta['Actual Effort (h)']}`",
        f"- **Estimated Cost (BRL):** `{meta['Estimated Cost (BRL)']}`",
        f"- **Actual Cost (BRL):** `{meta['Actual Cost (BRL)']}`",
        f"- **Planned Start:** `{meta['Planned Start']}`",
        f"- **Planned End:** `{meta['Planned End']}`",
        f"- **Actual Completion:** `{meta['Actual Completion']}`",
        f"- **Progress (%):** `{meta['Progress (%)']}`",
        f"- **Evidence:** {meta['Evidence']}",
        "",
        "### Relação com as categorias PSM",
        "- **Calendário e progresso:** Status, Planned/Actual dates, Progress (%), labels `status:*`.",
        "- **Recursos e custos:** Planned/Actual Effort (h) e Cost (BRL) com R$ 35,00/h.",
        "- **Desempenho dos processos:** Activity Type + evidências de fluxo (cycle time / throughput).",
        MARKER_END,
    ]
    return "\n".join(lines)


def desired_labels(existing: list[str], meta_labels: dict) -> list[str]:
    keep = [
        n
        for n in existing
        if not (
            n.startswith("psm:")
            or n.startswith("type:")
            or n.startswith("status:")
            or n.startswith("priority:")
            or n.startswith("environment:")
        )
    ]
    ordered = [
        meta_labels["psm"],
        meta_labels["type"],
        meta_labels["status"],
        meta_labels["priority"],
        meta_labels["env"],
    ]
    # preserve quality:* if already present
    keep = [n for n in keep if n.startswith("quality:") or n not in ordered]
    return ordered + [n for n in keep if n not in ordered]


def main():
    token = get_token()
    csv_rows = load_csv()
    issues = list_issues(token)
    mapping_rows = []
    updated = 0

    for issue in sorted(issues, key=lambda x: x["number"]):
        num = issue["number"]
        body = issue.get("body") or ""
        title = issue.get("title") or ""
        state = issue["state"]
        existing = [l["name"] for l in issue.get("labels", [])]
        aid = infer_activity_id(issue, body)
        crow = csv_rows.get(aid, {})

        prazo = dig(body, "Prazo planejado") or crow.get("prazo", "")
        corte = dig(body, "Corte de medição (calendário)") or crow.get("data_corte", "")
        csv_status = crow.get("status", "")
        if not csv_status:
            m = re.search(r"\*\*Status em[^:]*:\*\*\s*\*\*([^*]+)\*\*", body)
            txt = (m.group(1).strip().lower() if m else "")
            if "parcial" in txt:
                csv_status = "parcial"
            elif "pendente" in txt:
                csv_status = "pendente"
            elif state == "closed":
                csv_status = "concluida"
        evidencia = crow.get("evidencia_planilha_ou_ata") or dig(body, "Evidência", "Evidence")
        if not evidencia and state == "closed":
            evidencia = "Ver comentários, commits e entregáveis vinculados à issue"

        proj = project_status(csv_status, state)
        status_lbl = map_status_label(
            csv_status, crow.get("concluida_no_prazo", ""), state
        )
        psm_lbl = next(
            (n for n in existing if n.startswith("psm:")),
            psm_label_from_id(aid, title),
        )
        type_lbl = type_label_from_existing(existing, title)
        pri_lbl = priority_label(existing)
        env_lbl = env_label(existing)

        planned_effort = dig(body, "Esforço planejado (horas)", "Esforço planejado (h)")
        actual_effort = dig(body, "Esforço real (horas)", "Esforço real (h)")
        # esforço por issue não está no CSV de calendário; deixa em branco se ausente
        est_cost = (
            f"{float(planned_effort.replace(',', '.')) * COST_PER_HOUR:.2f}"
            if planned_effort
            else ""
        )
        act_cost = (
            f"{float(actual_effort.replace(',', '.')) * COST_PER_HOUR:.2f}"
            if actual_effort
            else ""
        )

        meta = {
            "Status": proj,
            "Priority": {"priority:high": "P0", "priority:medium": "P1", "priority:low": "P2"}.get(
                pri_lbl, "P1"
            ),
            "Quality Attribute": "Transversal ao estudo",
            "Activity Type": type_lbl.replace("type:", "").replace("-", " ").title(),
            "Platform": "Docs / Geral",
            "Planned Effort (h)": planned_effort or "(registrar na abertura)",
            "Actual Effort (h)": actual_effort or ("(registrar no fechamento)" if proj != "Done" else "(registrar)"),
            "Estimated Cost (BRL)": est_cost or "(H_p × 35)",
            "Actual Cost (BRL)": act_cost or "(H_r × 35)",
            "Planned Start": corte or "(AAAA-MM-DD)",
            "Planned End": prazo or "(AAAA-MM-DD)",
            "Actual Completion": prazo if proj == "Done" else "",
            "Progress (%)": progress_pct(proj),
            "Evidence": evidencia or "(caminho ou link)",
        }

        new_labels = desired_labels(
            existing,
            {
                "psm": psm_lbl,
                "type": type_lbl,
                "status": status_lbl,
                "priority": pri_lbl,
                "env": env_lbl,
            },
        )

        clean = strip_old_block(body)
        new_body = clean + "\n\n" + build_block(meta) + "\n"

        mapping_rows.append(
            {
                "number": num,
                "title": title,
                "activity_id": aid,
                "Status": meta["Status"],
                "status_label": status_lbl,
                "psm_label": psm_lbl,
                "Planned End": meta["Planned End"],
                "Progress (%)": meta["Progress (%)"],
                "labels": ",".join(new_labels),
            }
        )

        body_changed = new_body.strip() != (body or "").strip()
        labels_changed = set(new_labels) != set(existing)
        if not body_changed and not labels_changed:
            print(f"#{num} ok (sem alteração)")
            continue

        print(f"#{num} atualizando body={body_changed} labels={labels_changed}")
        if DRY_RUN:
            continue
        payload = {}
        if body_changed:
            payload["body"] = new_body
        if labels_changed:
            payload["labels"] = new_labels
        api("PATCH", f"/repos/{OWNER}/{REPO}/issues/{num}", token, payload)
        updated += 1

    out_csv = ROOT / "docs" / "gestao-psm" / "mapeamento-campos-issues.csv"
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(mapping_rows[0].keys()))
        w.writeheader()
        w.writerows(mapping_rows)

    print(f"Atualizadas: {updated}/{len(issues)}")
    print(f"CSV: {out_csv}")


if __name__ == "__main__":
    main()
