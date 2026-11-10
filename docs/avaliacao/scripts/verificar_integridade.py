#!/usr/bin/env python3
"""
verificar_integridade.py
Compara duas coleções Anki (ou um .apkg e uma coleção viva) e reporta diferenças.
Saída: CSV com contagens e hashes por entidade.
Uso:
  python scripts/verificar_integridade.py --antes caminho/para/colecao_antes --depois caminho/para/colecao_depois --saida diff.csv
"""
#Como usar: Comparar duas coleções (pastas com collection.anki2)
# python scripts/verificar_integridade.py --antes ~/anki_antes/collection.anki2 --depois ~/anki_depois/collection.anki2 --saida diff.csv
# Comparar um .apkg exportado com a coleção importada
#python scripts/verificar_integridade.py --antes export.apkg --depois ~/anki_importado/collection.anki2 --saida diff.csv


import argparse
import csv
import hashlib
import json
import os
import sqlite3
import sys
import zipfile
from pathlib import Path

# ---------- utilitários ----------

def hash_arquivo(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(65536), b""):
            h.update(bloco)
    return h.hexdigest()

def hash_texto(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()

def normalizar(valor):
    """Converte bytes/None para string comparável."""
    if valor is None:
        return ""
    if isinstance(valor, bytes):
        return valor.decode("utf-8", errors="replace")
    return str(valor)

# ---------- extração via pacote anki (se disponível) ----------

def snapshot_com_anki(caminho):
    try:
        from anki.collection import Collection
    except ImportError:
        return None

    col = Collection(caminho)
    try:
        snap = {
            "fonte": "anki_api",
            "notas": {},
            "cards": {},
            "baralhos": {},
            "revisoes": {},
            "midia": {},
        }

        # Notas
        for nid, mid, flds, tags in col.db.execute(
            "SELECT id, mid, flds, tags FROM notes"
        ):
            snap["notas"][nid] = {
                "mid": mid,
                "flds_hash": hash_texto(normalizar(flds)),
                "tags_hash": hash_texto(normalizar(tags)),
            }

        # Cards
        for cid, nid, did, ord_, due, ivl, factor, reps, lapses in col.db.execute(
            "SELECT id, nid, did, ord, due, ivl, factor, reps, lapses FROM cards"
        ):
            snap["cards"][cid] = {
                "nid": nid,
                "did": did,
                "ord": ord_,
                "due": due,
                "ivl": ivl,
                "factor": factor,
                "reps": reps,
                "lapses": lapses,
            }

        # Baralhos
        for did, name in col.db.execute("SELECT id, name FROM decks"):
            snap["baralhos"][did] = {"name": normalizar(name)}

        # Revisões (revlog)
        for rid, cid, ease, ivl, lastIvl, factor, time, type_ in col.db.execute(
            "SELECT id, cid, ease, ivl, lastIvl, factor, time, type FROM revlog"
        ):
            snap["revisoes"][rid] = {
                "cid": cid,
                "ease": ease,
                "ivl": ivl,
                "lastIvl": lastIvl,
                "factor": factor,
                "time": time,
                "type": type_,
            }

        # Mídia (pasta media/)
        media_dir = Path(caminho).parent / "collection.media"
        if media_dir.exists():
            for arq in media_dir.rglob("*"):
                if arq.is_file():
                    rel = str(arq.relative_to(media_dir))
                    snap["midia"][rel] = hash_arquivo(arq)

        return snap
    finally:
        col.close()

# ---------- extração via SQLite direto (fallback) ----------

def snapshot_sqlite(caminho):
    conn = sqlite3.connect(caminho)
    snap = {
        "fonte": "sqlite",
        "notas": {},
        "cards": {},
        "baralhos": {},
        "revisoes": {},
        "midia": {},
    }
    try:
        cur = conn.cursor()

        cur.execute("SELECT id, mid, flds, tags FROM notes")
        for nid, mid, flds, tags in cur.fetchall():
            snap["notas"][nid] = {
                "mid": mid,
                "flds_hash": hash_texto(normalizar(flds)),
                "tags_hash": hash_texto(normalizar(tags)),
            }

        cur.execute(
            "SELECT id, nid, did, ord, due, ivl, factor, reps, lapses FROM cards"
        )
        for cid, nid, did, ord_, due, ivl, factor, reps, lapses in cur.fetchall():
            snap["cards"][cid] = {
                "nid": nid,
                "did": did,
                "ord": ord_,
                "due": due,
                "ivl": ivl,
                "factor": factor,
                "reps": reps,
                "lapses": lapses,
            }

        cur.execute("SELECT id, name FROM decks")
        for did, name in cur.fetchall():
            snap["baralhos"][did] = {"name": normalizar(name)}

        cur.execute(
            "SELECT id, cid, ease, ivl, lastIvl, factor, time, type FROM revlog"
        )
        for rid, cid, ease, ivl, lastIvl, factor, time, type_ in cur.fetchall():
            snap["revisoes"][rid] = {
                "cid": cid,
                "ease": ease,
                "ivl": ivl,
                "lastIvl": lastIvl,
                "factor": factor,
                "time": time,
                "type": type_,
            }

    finally:
        conn.close()

    # Mídia
    media_dir = Path(caminho).parent / "collection.media"
    if media_dir.exists():
        for arq in media_dir.rglob("*"):
            if arq.is_file():
                rel = str(arq.relative_to(media_dir))
                snap["midia"][rel] = hash_arquivo(arq)

    return snap

# ---------- extração de .apkg (zip) ----------

def snapshot_apkg(caminho):
    snap = {
        "fonte": "apkg",
        "notas": {},
        "cards": {},
        "baralhos": {},
        "revisoes": {},
        "midia": {},
    }
    with zipfile.ZipFile(caminho, "r") as z:
        # O .apkg contém collection.anki2 (SQLite) e media/
        with z.open("collection.anki2") as f:
            tmp = Path("/tmp/_apkg_collection.anki2")
            tmp.write_bytes(f.read())
            snap_sqlite = snapshot_sqlite(str(tmp))
            tmp.unlink()
            snap.update(snap_sqlite)
            snap["fonte"] = "apkg"

        # Mídia dentro do zip
        for nome in z.namelist():
            if nome.startswith("media/") and not nome.endswith("/"):
                conteudo = z.read(nome)
                snap["midia"][nome] = hashlib.sha256(conteudo).hexdigest()

    return snap

# ---------- comparação ----------

def comparar(antes, depois):
    diffs = []

    def comparar_entidade(entidade):
        ids_antes = set(antes[entidade].keys())
        ids_depois = set(depois[entidade].keys())
        faltando = ids_antes - ids_depois
        extras = ids_depois - ids_antes
        for i in faltando:
            diffs.append({"entidade": entidade, "tipo": "faltando_no_depois", "id": i})
        for i in extras:
            diffs.append({"entidade": entidade, "tipo": "extra_no_depois", "id": i})
        for i in ids_antes & ids_depois:
            if antes[entidade][i] != depois[entidade][i]:
                diffs.append(
                    {
                        "entidade": entidade,
                        "tipo": "valor_diferente",
                        "id": i,
                        "antes": json.dumps(antes[entidade][i], sort_keys=True),
                        "depois": json.dumps(depois[entidade][i], sort_keys=True),
                    }
                )

    for ent in ["notas", "cards", "baralhos", "revisoes", "midia"]:
        comparar_entidade(ent)

    return diffs

# ---------- main ----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--antes", required=True, help="Caminho da coleção/.apkg antes")
    parser.add_argument("--depois", required=True, help="Caminho da coleção/.apkg depois")
    parser.add_argument("--saida", default="diff.csv", help="CSV de saída")
    args = parser.parse_args()

    def carregar(caminho):
        p = Path(caminho)
        if p.suffix == ".apkg":
            return snapshot_apkg(p)
        # Tenta API do anki; se falhar, SQLite direto
        snap = snapshot_com_anki(str(p))
        if snap is None:
            # Verifica se é um arquivo SQLite válido
            try:
                conn = sqlite3.connect(p)
                conn.execute("SELECT 1 FROM notes LIMIT 1")
                conn.close()
            except Exception:
                print(f"[ERRO] {p} não é uma coleção válida.", file=sys.stderr)
                sys.exit(1)
            snap = snapshot_sqlite(p)
        return snap

    print("Extraindo snapshot ANTES...")
    antes = carregar(args.antes)
    print("Extraindo snapshot DEPOIS...")
    depois = carregar(args.depois)

    diffs = comparar(antes, depois)

    with open(args.saida, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["entidade", "tipo", "id", "antes", "depois"],
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(diffs)

    print(f"Diferenças encontradas: {len(diffs)}")
    print(f"CSV salvo em: {args.saida}")

if __name__ == "__main__":
    main()