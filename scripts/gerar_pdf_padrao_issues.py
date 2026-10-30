"""Gera PDF didático alinhado à estrutura atual do repositório Betty Snyder."""
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "gestao-psm" / "padrao-abertura-fechamento-issues-psm.pdf"

NAVY = HexColor("#1B3A4B")
TEAL = HexColor("#2A6F7F")
LIGHT = HexColor("#E8F1F4")
DARK = HexColor("#222222")
CODE_BG = HexColor("#F4F7F8")


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "t",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=15,
            textColor=NAVY,
            spaceAfter=6,
            alignment=TA_CENTER,
            leading=18,
        ),
        "sub": ParagraphStyle(
            "s",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=TEAL,
            alignment=TA_CENTER,
            spaceAfter=12,
            leading=12,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=12,
            textColor=NAVY,
            spaceBefore=12,
            spaceAfter=6,
            leading=15,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            textColor=TEAL,
            spaceBefore=8,
            spaceAfter=4,
            leading=13,
        ),
        "body": ParagraphStyle(
            "b",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=DARK,
            alignment=TA_JUSTIFY,
            leading=13,
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "bu",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=DARK,
            leading=12,
            leftIndent=2,
        ),
        "small": ParagraphStyle(
            "sm",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=HexColor("#555555"),
            alignment=TA_CENTER,
            spaceBefore=10,
        ),
        "cell": ParagraphStyle(
            "c",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10.5,
            textColor=DARK,
        ),
        "cellb": ParagraphStyle(
            "cb",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=10.5,
            textColor=NAVY,
        ),
        "code": ParagraphStyle(
            "code",
            parent=base["Code"],
            fontName="Courier",
            fontSize=7.5,
            leading=10,
            textColor=DARK,
            backColor=CODE_BG,
            leftIndent=4,
            rightIndent=4,
            spaceBefore=4,
            spaceAfter=6,
            alignment=TA_LEFT,
        ),
    }


def bullets(items, st):
    return ListFlowable(
        [ListItem(Paragraph(i, st["bullet"]), leftIndent=10, bulletColor=TEAL) for i in items],
        bulletType="bullet",
        start="•",
        leftIndent=14,
        spaceBefore=1,
        spaceAfter=6,
    )


def table(data, col_widths, st):
    formatted = []
    for i, row in enumerate(data):
        style = st["cellb"] if i == 0 else st["cell"]
        formatted.append([Paragraph(str(c), style) for c in row])
    t = Table(formatted, colWidths=col_widths, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("TEXTCOLOR", (0, 0), (-1, 0), NAVY),
                ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#9BB8C2")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return t


def build():
    st = styles()
    story = []

    story.append(Paragraph("Padrão de abertura e fechamento de Issues", st["title"]))
    story.append(
        Paragraph(
            "Equipe Betty Snyder · repositório 2026-2_T01_BETTY_SNYDER · PSM/CID · 30/10/2026",
            st["sub"],
        )
    )
    story.append(
        Paragraph(
            "Guia objetivo alinhado à estrutura <b>atual</b> do repositório: pastas, "
            "templates em <b>.github/ISSUE_TEMPLATE/</b>, corpo das Issues, labels, "
            "milestones, Project <b>Anki Quality Assessment: PSM/CID</b> e páginas "
            "MkDocs em <b>docs/gestao-psm/</b>.",
            st["body"],
        )
    )

    # 1 Estrutura
    story.append(Paragraph("1. Estrutura atual do repositório (o que importa para Issues)", st["h1"]))
    story.append(
        Preformatted(
            "2026-2_T01_BETTY_SNYDER/\n"
            "├── .github/ISSUE_TEMPLATE/     templates 01, 02, 03 + config.yml\n"
            "├── docs/                      MkDocs (GitPages)\n"
            "│   ├── gestao-psm.md          visão geral PSM\n"
            "│   └── gestao-psm/            categorias + github-organizacao + este PDF\n"
            "├── gestao-psm/                CSV/XLSX da série histórica (E1)\n"
            "├── scripts/                   setup-github-project.ps1, sync-issue-fields.py\n"
            "└── mkdocs.yml                 navegação Gestão PSM",
            st["code"],
        )
    )
    story.append(
        Paragraph(
            "As Issues materializam tarefas (entidades PSM). Os atributos medidos "
            "estão no <b>corpo da Issue</b> e devem ser espelhados nos campos do "
            "Project. A série E1 continua em <b>gestao-psm/*.csv</b>; a documentação "
            "interpretativa está em <b>docs/gestao-psm/</b>.",
            st["body"],
        )
    )

    # 2 Ideia central
    story.append(Paragraph("2. Ideia central", st["h1"]))
    story.append(
        Paragraph(
            "<b>PSM</b> mede o processo/gestão do projeto (esforço, prazo, fluxo, "
            "eficácia). <b>GQM</b> mede o produto Anki. Não misture as duas fontes.",
            st["body"],
        )
    )
    story.append(
        table(
            [
                ["Instrumento", "Papel"],
                ["Template 01 - Atividade de Avaliação", "Tarefa do projeto (fonte PSM)"],
                ["Template 02 - Registro de Medição", "Observação GQM do Anki (produto)"],
                ["Template 03 - Recomendação de Melhoria", "Ação de melhoria"],
                ["Project Anki Quality Assessment: PSM/CID", "Campos numéricos e Status de fluxo"],
                ["Labels psm:* / type:* / status:*", "Filtro e corte de conformidade"],
            ],
            [7.8 * cm, 8.9 * cm],
            st,
        )
    )

    # 3 Estrutura da Issue
    story.append(Paragraph("3. Estrutura da Issue (usar diretamente)", st["h1"]))
    story.append(
        Paragraph(
            "As Issues do repositório seguem este corpo. Não há formulário paralelo: "
            "preencha e mantenha esta estrutura; espelhe o bloco final no Project.",
            st["body"],
        )
    )
    story.append(
        Preformatted(
            "## Identificação\n"
            "- **ID da atividade:** `E2-A1`\n"
            "- **Responsável:** Dupla A\n"
            "- **Prazo planejado:** AAAA-MM-DD\n"
            "- **Corte de medição (calendário):** AAAA-MM-DD\n"
            "- **Fonte de planejamento:** ...\n"
            "## Objetivo\n"
            "...\n"
            "## Situação atualizada (corte ...)\n"
            "- **Campo `status` (CSV):** `pendente|parcial|concluida`\n"
            "- **Concluída no prazo:** `sim|nao`\n"
            "- **Evidência:** ...\n"
            "## Critérios de conclusão\n"
            "- [ ] ...\n"
            "## Observações PSM/CID\n"
            "...\n"
            "## Campos do Project (PSM)\n"
            "- **Status:** `Todo|In Progress|Done`\n"
            "- **Priority / Quality Attribute / Activity Type / Platform**\n"
            "- **Planned|Actual Effort (h)** e **Estimated|Actual Cost (BRL)**\n"
            "- **Planned Start|End**, **Actual Completion**, **Progress (%)**, **Evidence**",
            st["code"],
        )
    )
    story.append(
        Paragraph(
            "Labels mínimas em Issues de atividade: uma <b>psm:*</b>, uma <b>type:*</b>, "
            "uma <b>priority:*</b>, <b>environment:*</b> quando couber, e "
            "<b>status:pending|partial|on-time|late</b> conforme o corte.",
            st["body"],
        )
    )

    # 4 Abrir
    story.append(Paragraph("4. Abrir uma Issue (passo a passo)", st["h1"]))
    story.append(Paragraph("4.1 Escolher o template", st["h2"]))
    story.append(
        table(
            [
                ["Arquivo", "Nome no GitHub", "Prefixo"],
                ["01-activity.yml", "01 - Atividade de Avaliação", "[TASK]"],
                ["02-measurement.yml", "02 - Registro de Medição", "[MEAS]"],
                ["03-improvement.yml", "03 - Recomendação de Melhoria", "[IMPROVE]"],
            ],
            [4.2 * cm, 7.5 * cm, 5 * cm],
            st,
        )
    )
    story.append(Paragraph("4.2 Depois de criar", st["h2"]))
    story.append(
        bullets(
            [
                "Associar à milestone: <b>F1 | Plano de Medição e Preparação</b>, "
                "<b>F2 | Execução e Análise das Medições</b> ou "
                "<b>E2 | Relatório e Recomendações de Melhoria</b> (PC1 já closed).",
                "Incluir no Project e definir Status: <b>Todo</b> (A Fazer) ou "
                "<b>In Progress</b> (Em Andamento).",
                "Preencher no Project os mesmos campos do bloco <b>Campos do Project (PSM)</b>.",
                "Custo: <b>Estimated Cost (BRL) = Planned Effort (h) × 35</b>.",
                "Assignee + labels coerentes com o padrão do repositório.",
            ],
            st,
        )
    )
    story.append(Paragraph("4.3 Campos do Project (nomes exatos)", st["h2"]))
    story.append(
        table(
            [
                ["Campo", "Tipo / valores"],
                ["Status", "Todo · In Progress · Done"],
                ["Priority", "High · Medium · Low"],
                ["Quality Attribute", "Interaction Capability · Performance Efficiency · Flexibility · Cross-cutting"],
                ["Activity Type", "Planning · Execution · Measurement · Analysis · Documentation · Improvement"],
                ["Platform", "Desktop Windows · Desktop macOS · Desktop Ubuntu · AnkiWeb · Cross-platform"],
                ["Planned / Actual Effort (h)", "número (Hp / Hr)"],
                ["Estimated / Actual Cost (BRL)", "número (H × 35)"],
                ["Planned Start / Planned End", "data"],
                ["Actual Completion", "data"],
                ["Progress (%)", "número"],
                ["Evidence", "texto (caminho ou link no repositório)"],
            ],
            [5.5 * cm, 11.2 * cm],
            st,
        )
    )
    story.append(
        Paragraph(
            "Não existe campo “Categoria PSM” no Project: a categoria é a pergunta "
            "respondida pelo conjunto de atributos (ver seção 7).",
            st["body"],
        )
    )

    # 5 Execução
    story.append(Paragraph("5. Durante a execução", st["h1"]))
    story.append(
        bullets(
            [
                "Status do Project → <b>In Progress</b> no primeiro dia de trabalho real.",
                "Atualizar Progress (%) e comentários com evidências parciais.",
                "Atualizar a seção <b>Situação atualizada</b> no corpo da Issue.",
                "Não apagar Planned End se houver atraso: registre o desvio em comentário.",
            ],
            st,
        )
    )

    # 6 Fechar
    story.append(Paragraph("6. Fechar uma Issue (passo a passo)", st["h1"]))
    story.append(
        bullets(
            [
                "Marcar critérios de conclusão e preencher <b>Evidence</b>.",
                "Actual Effort (h) = horas reais; Actual Cost (BRL) = Hr × 35.",
                "Actual Completion = data real; Progress (%) = 100; Status = <b>Done</b>.",
                "Label de prazo: <b>status:on-time</b> ou <b>status:late</b> "
                "(compare Actual Completion com Planned End / Prazo planejado).",
                "Atualizar Situação atualizada: status CSV <b>concluida</b> e "
                "Concluída no prazo sim/nao.",
                "Só então fechar a Issue (state closed) no GitHub.",
            ],
            st,
        )
    )

    story.append(PageBreak())

    # 7 PSM
    story.append(Paragraph("7. Relação com as categorias PSM (docs/gestao-psm/)", st["h1"]))
    story.append(
        Paragraph(
            "Os mesmos campos da Issue/Project alimentam as três páginas de categoria "
            "da GitPages. Abaixo: o que cada campo mede na prática da equipe.",
            st["body"],
        )
    )

    story.append(Paragraph("7.1 Calendário e progresso", st["h2"]))
    story.append(
        Paragraph(
            "Página: <b>docs/gestao-psm/calendario-e-progresso.md</b>. "
            "Medida central E1: <b>ICP</b> (índice de conformidade de prazos). "
            "Fluxo futuro: Cycle Time, Throughput, WIP.",
            st["body"],
        )
    )
    story.append(
        table(
            [
                ["Campo / evidência na Issue", "Medição"],
                ["Prazo planejado · Planned End · Actual Completion", "Base do ICP (no prazo ou atrasado)"],
                ["Status Todo → In Progress → Done", "Fluxo, WIP, cycle time"],
                ["Progress (%)", "Proxy de avanço da unidade de trabalho"],
                ["Labels status:on-time|late|partial|pending", "Corte de conformidade"],
                ["Milestone F1 / F2 / E2", "Work items comprometidos vs concluídos"],
                ["CSV gestao-psm/calendario-progresso.csv", "Série histórica E1"],
            ],
            [8.2 * cm, 8.5 * cm],
            st,
        )
    )

    story.append(Paragraph("7.2 Recursos e custos", st["h2"]))
    story.append(
        Paragraph(
            "Página: <b>docs/gestao-psm/recursos-e-custos.md</b>. "
            "Convenção: <b>C = H × 35</b> (R$ 35,00/h). Hp = Planned Effort; Hr = Actual Effort.",
            st["body"],
        )
    )
    story.append(
        table(
            [
                ["Campo / evidência na Issue", "Medição"],
                ["Planned Effort (h) = Hp", "Esforço planejado"],
                ["Actual Effort (h) = Hr", "Esforço real"],
                ["Estimated Cost (BRL) = Hp × 35", "Custo estimado"],
                ["Actual Cost (BRL) = Hr × 35", "Custo real"],
                ["CSV gestao-psm/recursos-custos.csv (+ planilha de horas)", "Série E1 por integrante/dupla"],
            ],
            [8.2 * cm, 8.5 * cm],
            st,
        )
    )

    story.append(Paragraph("7.3 Desempenho dos processos", st["h2"]))
    story.append(
        Paragraph(
            "Página: <b>docs/gestao-psm/desempenho-dos-processos.md</b>. "
            "Eixo A (E1): densidade de defeitos D e taxa de correção "
            "(CSV desempenho-processos.csv). Eixo B: trabalho planejado / concluído / em aberto.",
            st["body"],
        )
    )
    story.append(
        table(
            [
                ["Campo / evidência na Issue", "Medição"],
                ["Datas + Status de fluxo", "Tendência de execução e cycle time"],
                ["Activity Type", "Perfil do trabalho no processo"],
                ["Template 03 / type:improvement", "Ações de correção / retrabalho"],
                ["Evidence + revisões documentadas", "Apoio a D e taxa de correção"],
                ["Contagem open vs closed por milestone", "Trabalho em aberto vs concluído"],
            ],
            [8.2 * cm, 8.5 * cm],
            st,
        )
    )

    story.append(Paragraph("7.4 Mapa rápido campo → categoria", st["h2"]))
    story.append(
        table(
            [
                ["Campo", "Calendário", "Recursos", "Desempenho"],
                ["Status (fluxo)", "Sim", "Nao", "Sim"],
                ["Planned/Actual dates", "Sim", "Nao", "Sim"],
                ["Progress (%)", "Sim", "Nao", "Apoio"],
                ["Labels status:*", "Sim", "Nao", "Apoio"],
                ["Planned/Actual Effort", "Nao", "Sim", "Apoio"],
                ["Estimated/Actual Cost", "Nao", "Sim", "Nao"],
                ["Activity Type", "Nao", "Nao", "Sim"],
                ["Evidence", "Apoio", "Apoio", "Apoio"],
            ],
            [5.0 * cm, 3.9 * cm, 3.9 * cm, 3.9 * cm],
            st,
        )
    )

    # 8 Labels e milestones
    story.append(Paragraph("8. Labels e milestones do repositório", st["h1"]))
    story.append(
        table(
            [
                ["Família", "Valores em uso"],
                ["psm:*", "process-performance · resources-cost · schedule-progress"],
                ["type:*", "planning · execution · measurement · analysis · documentation · improvement"],
                ["priority:*", "high · medium · low"],
                ["environment:*", "desktop · web · cross-platform"],
                ["quality:*", "interaction · performance · flexibility"],
                ["status:*", "on-time · late · partial · pending"],
            ],
            [3.8 * cm, 12.9 * cm],
            st,
        )
    )
    story.append(
        Paragraph(
            "Há labels legadas (ex.: Característica: Usabilidade; PSM: Recursos-Custos). "
            "Novas Issues usam o vocabulário com prefixo do padrão (psm:, quality:, type:).",
            st["body"],
        )
    )
    story.append(
        table(
            [
                ["#", "Milestone", "Due"],
                ["1", "PC1", "19/10/2026 (closed)"],
                ["2", "F1 | Plano de Medição e Preparação", "26/10/2026"],
                ["3", "F2 | Execução e Análise das Medições", "11/11/2026"],
                ["4", "E2 | Relatório e Recomendações de Melhoria", "18/11/2026"],
            ],
            [1.2 * cm, 11.2 * cm, 4.3 * cm],
            st,
        )
    )

    # 9 Exemplo fiel
    story.append(Paragraph("9. Exemplo alinhado ao repositório", st["h1"]))
    story.append(
        Paragraph(
            "<b>Abertura:</b> título <b>[TASK] E2-B1 - Protocolo de sync AnkiWeb</b>; "
            "template 01; milestone F2; labels "
            "psm:schedule-progress, type:execution, environment:web, priority:medium, "
            "status:pending; Planned Effort 3 h → Estimated Cost 105; "
            "Platform AnkiWeb; Status Todo; bloco Campos do Project preenchido.",
            st["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Fechamento:</b> Actual Effort 4 h → Actual Cost 140; "
            "Actual Completion um dia após Planned End → status:late; "
            "Evidence apontando arquivo em gestao-psm/ ou docs/; "
            "Progress 100; Status Done; Situação atualizada = concluida; fechar Issue.",
            st["body"],
        )
    )

    # 10 Onde ler
    story.append(Paragraph("10. Onde completar a leitura", st["h1"]))
    story.append(
        bullets(
            [
                "docs/gestao-psm.md e docs/gestao-psm/{recursos-e-custos,calendario-e-progresso,desempenho-dos-processos}.md",
                "docs/gestao-psm/github-organizacao.md (Project, labels, milestones, templates)",
                "gestao-psm/*.csv (série Entrega 1)",
                "scripts/setup-github-project.ps1 (definição dos campos do Project)",
                "scripts/sync-issue-fields.py (bloco Campos do Project no corpo das Issues)",
                "GitPages: site Gestão PSM na navegação MkDocs",
            ],
            st,
        )
    )

    story.append(
        Paragraph(
            "Betty Snyder · FGA0315 Qualidade de Software 1 · UnB/FGA · PDF gerado a partir da estrutura do repositório em 30/10/2026",
            st["small"],
        )
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title="Padrão de abertura e fechamento de Issues (PSM)",
        author="Equipe Betty Snyder",
    )
    doc.build(story)
    print(f"PDF gerado: {OUT}")


if __name__ == "__main__":
    build()
