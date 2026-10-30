"""Gera PDF didático: abertura/fechamento de issues e relação com PSM."""
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
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


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "t",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=16,
            textColor=NAVY,
            spaceAfter=8,
            alignment=TA_CENTER,
            leading=20,
        ),
        "sub": ParagraphStyle(
            "s",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            textColor=TEAL,
            alignment=TA_CENTER,
            spaceAfter=16,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=13,
            textColor=NAVY,
            spaceBefore=14,
            spaceAfter=8,
            leading=16,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=TEAL,
            spaceBefore=10,
            spaceAfter=6,
            leading=14,
        ),
        "body": ParagraphStyle(
            "b",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            textColor=DARK,
            alignment=TA_JUSTIFY,
            leading=14,
            spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "bu",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            textColor=DARK,
            leading=13,
            leftIndent=4,
        ),
        "small": ParagraphStyle(
            "sm",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=HexColor("#555555"),
            alignment=TA_CENTER,
            spaceBefore=12,
        ),
        "cell": ParagraphStyle(
            "c",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            textColor=DARK,
        ),
        "cellb": ParagraphStyle(
            "cb",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.5,
            leading=11,
            textColor=NAVY,
        ),
    }


def bullets(items, st):
    return ListFlowable(
        [ListItem(Paragraph(i, st["bullet"]), leftIndent=12, bulletColor=TEAL) for i in items],
        bulletType="bullet",
        start="•",
        leftIndent=15,
        spaceBefore=2,
        spaceAfter=8,
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
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
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
            "Equipe Betty Snyder · Avaliação Anki com PSM/CID · 2026-2",
            st["sub"],
        )
    )
    story.append(
        Paragraph(
            "Este guia resume, de forma objetiva, como abrir e fechar Issues no "
            "repositório <b>2026-2_T01_BETTY_SNYDER</b> e como cada campo alimenta "
            "as medições das três categorias PSM: <b>Calendário e Progresso</b>, "
            "<b>Recursos e Custos</b> e <b>Desempenho dos Processos</b>.",
            st["body"],
        )
    )

    story.append(Paragraph("1. Ideia central", st["h1"]))
    story.append(
        Paragraph(
            "Não misture qualidade do produto Anki com desempenho do processo da "
            "equipe. Issues de atividade (template 01) medem o <b>processo</b> "
            "(PSM). Issues de medição (template 02) registram observações do "
            "<b>produto</b> (GQM). O Project "
            "<b>Anki Quality Assessment: PSM/CID</b> concentra os campos "
            "numéricos e de fluxo. Labels e o corpo da Issue documentam a "
            "mesma informação para rastreio.",
            st["body"],
        )
    )
    story.append(
        Paragraph(
            "Regra prática: cada Issue de atividade deve ter uma label "
            "<b>psm:*</b>, uma <b>type:*</b> e, quando fizer sentido, "
            "<b>quality:*</b> / <b>environment:*</b>. O Status do Project "
            "(Todo / In Progress / Done) descreve o fluxo; as labels "
            "<b>status:on-time | late | partial | pending</b> descrevem "
            "conformidade de prazo no corte.",
            st["body"],
        )
    )

    story.append(Paragraph("2. Abrir uma Issue (passo a passo)", st["h1"]))
    story.append(Paragraph("2.1 Escolher o template", st["h2"]))
    story.append(
        table(
            [
                ["Template", "Quando usar"],
                ["01 - Atividade", "Planejar/executar tarefa do estudo (fonte PSM)"],
                ["02 - Medição", "Registrar observação GQM do Anki (produto)"],
                ["03 - Melhoria", "Ação decorrente de resultado abaixo do alvo"],
            ],
            [4.2 * cm, 12.5 * cm],
            st,
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph("2.2 Depois de criar a Issue", st["h2"]))
    story.append(
        Paragraph(
            "Não há formulário intermediário: use diretamente a estrutura da Issue "
            "(título, corpo, labels e bloco <b>Campos do Project (PSM)</b>) e "
            "espelhe os valores no quadro.",
            st["body"],
        )
    )
    story.append(
        bullets(
            [
                "Associar à <b>milestone</b> correta (F1, F2 ou E2).",
                "Incluir no Project e definir <b>Status = Todo</b> (ou In Progress se já começou).",
                "Preencher no Project os campos já documentados na Issue: Planned Effort, Planned Start/End, Priority, Activity Type, Platform.",
                "Calcular <b>Estimated Cost (BRL) = esforço planejado × 35</b>.",
                "Atribuir responsável (assignee) e manter labels coerentes.",
                "Manter o bloco <b>Campos do Project (PSM)</b> no corpo alinhado ao quadro.",
            ],
            st,
        )
    )

    story.append(Paragraph("3. Durante a execução", st["h1"]))
    story.append(
        bullets(
            [
                "Mover Status do Project para <b>In Progress</b> no primeiro dia de trabalho real.",
                "Registrar evidências parciais em comentários (links, caminhos, prints).",
                "Atualizar Progress (%) (ex.: 25 / 50 / 75) sem inventar dados.",
                "Se o prazo estiver em risco, comentar o desvio; não apagar o Planned End.",
            ],
            st,
        )
    )

    story.append(Paragraph("4. Fechar uma Issue (passo a passo)", st["h1"]))
    story.append(
        bullets(
            [
                "Conferir critérios de conclusão e anexar/apontar a <b>Evidence</b>.",
                "Preencher <b>Actual Effort (h)</b> (horas reais da tarefa).",
                "Calcular <b>Actual Cost (BRL) = esforço real × 35</b>.",
                "Preencher <b>Actual Completion</b> com a data real de término.",
                "Progress (%) = 100; Status do Project = <b>Done</b>.",
                "Ajustar label de prazo: <b>status:on-time</b> ou <b>status:late</b> "
                "(compare Actual Completion com Planned End).",
                "Fechar a Issue no GitHub (state closed) somente após os campos acima.",
            ],
            st,
        )
    )
    story.append(
        Paragraph(
            "Checklist mínimo de fechamento: entregável no repositório ou Overleaf, "
            "evidência citada, esforço real registrado, custo calculado, Status Done.",
            st["body"],
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("5. Relação dos campos com as categorias PSM", st["h1"]))
    story.append(
        Paragraph(
            "Os mesmos campos da Issue/Project alimentam as três necessidades de "
            "informação. Não é necessário um campo separado “Categoria PSM” no "
            "quadro: a categoria é a pergunta que você responde com o conjunto de "
            "atributos abaixo.",
            st["body"],
        )
    )

    story.append(Paragraph("5.1 Calendário e Progresso", st["h2"]))
    story.append(
        Paragraph(
            "Pergunta típica: estamos no prazo? Quanto trabalho avançou no corte?",
            st["body"],
        )
    )
    story.append(
        table(
            [
                ["Campo / evidência", "Uso na medição"],
                ["Planned End / Actual Completion", "Base do ICP (no prazo ou atrasado)"],
                ["Status Todo → In Progress → Done", "Fluxo, WIP e cycle time"],
                ["Progress (%)", "Proxy de avanço da unidade de trabalho"],
                ["Labels status:on-time/late/partial/pending", "Corte de conformidade de prazo"],
                ["Milestone (F1/F2/E2)", "Work items comprometidos vs concluídos"],
            ],
            [7.5 * cm, 9.2 * cm],
            st,
        )
    )

    story.append(Paragraph("5.2 Recursos e Custos", st["h2"]))
    story.append(
        Paragraph(
            "Pergunta típica: quanto esforço e custo consumimos frente ao plano?",
            st["body"],
        )
    )
    story.append(
        table(
            [
                ["Campo / evidência", "Uso na medição"],
                ["Planned Effort (h) = Hp", "Esforço planejado da atividade"],
                ["Actual Effort (h) = Hr", "Esforço real da atividade"],
                ["Estimated / Actual Cost (BRL)", "C = H × 35 (R$ 35,00 por hora)"],
                ["Soma por integrante / dupla", "Participação e desvio percentual"],
            ],
            [7.5 * cm, 9.2 * cm],
            st,
        )
    )
    story.append(
        Paragraph(
            "Convenção da equipe: sempre use R$ 35,00/h. Se o esforço ainda não "
            "foi informado na abertura, registre o valor assim que o responsável "
            "estimar a tarefa; no fechamento, atualize o valor real.",
            st["body"],
        )
    )

    story.append(Paragraph("5.3 Desempenho dos Processos", st["h2"]))
    story.append(
        Paragraph(
            "Pergunta típica: o processo de avaliação flui? Há retrabalho ou bloqueios?",
            st["body"],
        )
    )
    story.append(
        table(
            [
                ["Campo / evidência", "Uso na medição"],
                ["Datas de início/fim + Status", "Cycle time e throughput no período"],
                ["Activity Type", "Perfil do trabalho (execução, análise, doc…)"],
                ["Issues tipo Bug / Improvement", "Sinais de defeito ou retrabalho"],
                ["Evidence + comentários de bloqueio", "Análise qualitativa do fluxo"],
            ],
            [7.5 * cm, 9.2 * cm],
            st,
        )
    )

    story.append(Paragraph("6. Mapa rápido campo → categoria", st["h1"]))
    story.append(
        table(
            [
                ["Campo do Project", "Calendário", "Recursos", "Desempenho"],
                ["Status (fluxo)", "Sim", "Nao", "Sim"],
                ["Planned/Actual dates", "Sim", "Nao", "Sim"],
                ["Progress (%)", "Sim", "Nao", "Apoio"],
                ["Planned/Actual Effort", "Nao", "Sim", "Apoio"],
                ["Estimated/Actual Cost", "Nao", "Sim", "Nao"],
                ["Evidence", "Apoio", "Apoio", "Apoio"],
                ["Activity Type", "Nao", "Nao", "Sim"],
            ],
            [5.2 * cm, 3.8 * cm, 3.8 * cm, 3.9 * cm],
            st,
        )
    )

    story.append(Paragraph("7. Exemplos curtos", st["h1"]))
    story.append(Paragraph("Abertura", st["h2"]))
    story.append(
        Paragraph(
            "Título: <b>[TASK] E2-B1 — Coletar tempos de sync no AnkiWeb</b>. "
            "Labels: psm:schedule-progress, type:execution, environment:web. "
            "Planned Effort 3 h → Estimated Cost R$ 105,00. Planned End 2026-11-05. "
            "Status Todo. Milestone F2.",
            st["body"],
        )
    )
    story.append(Paragraph("Fechamento", st["h2"]))
    story.append(
        Paragraph(
            "Actual Effort 4 h → Actual Cost R$ 140,00. Actual Completion 2026-11-06 "
            "(1 dia após o plano) → label status:late. Evidence: "
            "data/raw/sync-ankiweb-run01.csv. Progress 100%. Status Done. Fechar Issue.",
            st["body"],
        )
    )

    story.append(Paragraph("8. Onde está a documentação completa", st["h1"]))
    story.append(
        bullets(
            [
                "GitPages: docs/gestao-psm/ (visão geral e páginas por categoria).",
                "Organização GitHub: docs/gestao-psm/github-organizacao.md.",
                "Padrão acadêmico: padrao_documentacao_github.md (pasta do projeto).",
                "CSV históricos: gestao-psm/*.csv (série Entrega 1).",
                "Script de sincronização do bloco de campos: scripts/sync-issue-fields.py.",
            ],
            st,
        )
    )

    story.append(
        Paragraph(
            "Betty Snyder · Qualidade de Software 1 · UnB/FGA · atualizado em 30/10/2026",
            st["small"],
        )
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.6 * cm,
        bottomMargin=1.6 * cm,
        title="Padrão de abertura e fechamento de Issues (PSM)",
        author="Equipe Betty Snyder",
    )
    doc.build(story)
    print(f"PDF gerado: {OUT}")


if __name__ == "__main__":
    build()
