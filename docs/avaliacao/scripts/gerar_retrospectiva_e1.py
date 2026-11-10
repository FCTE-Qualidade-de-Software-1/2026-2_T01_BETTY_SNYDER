"""Gera a Retrospectiva E1 (PDF) com métricas PSM da equipe na questão 4."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
)

OUT = Path(__file__).resolve().parents[1] / "docs" / "atas" / "2026-10-28_retrospectiva-e1.pdf"
OUT_DOWNLOADS = Path(r"C:\Users\pedro.rodrigues\Downloads\T01 T02 - E1 RETROSPECTIVA.pdf")


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            alignment=TA_JUSTIFY,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
        ),
        "cell": ParagraphStyle(
            "cell",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.5,
            leading=9.5,
            alignment=TA_LEFT,
        ),
        "cellb": ParagraphStyle(
            "cellb",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=7.5,
            leading=9.5,
        ),
        "footer": ParagraphStyle(
            "footer",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7,
            alignment=TA_CENTER,
            textColor=colors.grey,
        ),
    }


def p(text, style):
    return Paragraph(text.replace("\n", "<br/>"), style)


def build():
    s = styles()
    story = []

    story.append(p("Retrospectiva – Entrega 1", s["title"]))
    story.append(
        p(
            "<b>Equipe e projeto:</b> Betty Snyder - Anki"
            "&nbsp;&nbsp;&nbsp;&nbsp;<b>Turma:</b> 01"
            "&nbsp;&nbsp;&nbsp;&nbsp;<b>Data:</b> 28/10/2026",
            s["body"],
        )
    )
    story.append(Spacer(1, 4))

    integrantes = [
        ["Matrícula", "Nome"],
        ["_________________", "_______________________________________________"],
        ["_________________", "_______________________________________________"],
        ["231012156", "Bryan Smith Rodrigues Cavalcante"],
        ["222024372", "Dante Fernandes Scarpati"],
        ["241011018", "Davi Severiano Freitas"],
        ["231026545", "Pedro Henrique Freire Rodrigues"],
    ]
    t = Table(integrantes, colWidths=[3.2 * cm, 13.5 * cm])
    t.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.9, 0.9, 0.9)),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(t)
    story.append(Spacer(1, 4))
    story.append(
        p(
            "<b>Facilitador:</b> ______________________________"
            "&nbsp;&nbsp;&nbsp;<b>Relator:</b> Pedro Henrique Freire Rodrigues",
            s["body"],
        )
    )
    story.append(Spacer(1, 6))
    story.append(
        p(
            "Analisem a condução da primeira entrega e definam mudanças para a próxima etapa. "
            "Preencham no computador ou à mão. Se usarem papel, reúnam as fotos dos registros em um PDF.",
            s["small"],
        )
    )
    story.append(
        p(
            "A autoavaliação e a avaliação por pares são respondidas nos formulários. "
            "Não transcrevam suas respostas neste documento.",
            s["small"],
        )
    )

    # 1
    story.append(p("1 Tarefa 1 — O projeto como filme ou carro", s["h2"]))
    story.append(p("Se o seu projeto fosse um filme ou um carro, qual seria?", s["body"]))
    story.append(
        p(
            "<b>Carro ou filme:</b> Filme&nbsp;&nbsp;&nbsp;&nbsp;"
            "<b>Filme:</b> “Missão: Impossível”",
            s["body"],
        )
    )
    story.append(p("<b>Por quê?</b> (resposta curta):", s["body"]))
    story.append(
        p(
            "Comparando o projeto a um filme, podemos relacionar a “Missão: Impossível”, no sentido de que "
            "tivemos um planejamento bom; a execução ocorreu com entraves que não eram esperados, mas, "
            "no final, obtivemos uma entrega razoável.",
            s["body"],
        )
    )

    # 2
    story.append(p("2 Atividade 2", s["h2"]))
    story.append(
        p(
            "<b>O que, na nossa forma de trabalhar, colocou em risco ou impediu a conclusão da primeira fase?</b>",
            s["body"],
        )
    )
    story.append(
        p(
            "Subestimação do tempo necessário para concluir com êxito as tarefas e objetivos definidos; "
            "comunicação pouco constante em determinadas etapas da entrega em subequipes, no sentido de "
            "organizar com mais cuidado os prazos previstos de entregas; dificuldade de disponibilidade "
            "de todos os membros para participar das reuniões de organização da equipe.",
            s["body"],
        )
    )
    story.append(
        p(
            "<b>O que ajudou, mas precisa de ajustes para a próxima etapa?</b>",
            s["body"],
        )
    )
    story.append(
        p(
            "A organização e planejamento das atividades ocorreu via atas e documentos, o que contribuiu "
            "para o desenvolvimento da entrega da equipe, mas pode ser aprimorada via issues, para tornar "
            "mais visível todas as tarefas definidas e o status de cada uma.",
            s["body"],
        )
    )
    story.append(
        p(
            "<b>O que contribuiu para nossas entregas e devemos preservar?</b>",
            s["body"],
        )
    )
    story.append(
        p(
            "Devemos manter o padrão de qualidade de todos os integrantes nas próximas entregas, que foi "
            "satisfatório na primeira entrega; manter o uso ético da IA, não para produzir as entregas, "
            "mas para nos ajudar a entender o conteúdo teórico e, nas atividades, o que e como pode ser "
            "feito, bem como para ajudar na revisão dos resultados dos trabalhos feitos.",
            s["body"],
        )
    )

    # 3
    story.append(p("3 Priorização e análise", s["h2"]))
    story.append(
        p(
            "Após discutirem os registros das casas de palha, madeira e tijolos, cada integrante deverá "
            "votar em três tópicos diferentes que a equipe precisa priorizar para a próxima etapa.",
            s["small"],
        )
    )

    pri = [
        [
            p("<b>COD</b>", s["cellb"]),
            p("<b>Tópico</b>", s["cellb"]),
            p("<b>Votos</b>", s["cellb"]),
            p("<b>Priorizado?</b>", s["cellb"]),
        ],
        [
            p("C1", s["cell"]),
            p("Subestimação do tempo para produzir as tarefas", s["cell"]),
            p("Pedro, Davi, Bryan", s["cell"]),
            p("n", s["cell"]),
        ],
        [
            p("C2", s["cell"]),
            p(
                "Comunicação pouco constante entre pessoas da mesma dupla e entre duplas",
                s["cell"],
            ),
            p("Pedro, Dante, Bryan, Davi", s["cell"]),
            p("<b>s</b>", s["cell"]),
        ],
        [
            p("C3", s["cell"]),
            p("Pouca disponibilidade dos membros para reuniões", s["cell"]),
            p("—", s["cell"]),
            p("n", s["cell"]),
        ],
        [
            p("C4", s["cell"]),
            p("Formato de organização de tarefas", s["cell"]),
            p("Pedro, Dante, Bryan", s["cell"]),
            p("<b>s</b>", s["cell"]),
        ],
        [
            p("C5", s["cell"]),
            p("Qualidade das entregas", s["cell"]),
            p("Davi, Dante", s["cell"]),
            p("n", s["cell"]),
        ],
        [
            p("C6", s["cell"]),
            p("Uso ético da IA", s["cell"]),
            p("—", s["cell"]),
            p("n", s["cell"]),
        ],
    ]
    tp = Table(pri, colWidths=[1.2 * cm, 9.2 * cm, 4.2 * cm, 2.2 * cm])
    tp.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.4, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.9, 0.9, 0.9)),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(tp)
    story.append(
        p(
            "Obs.: Uma entrega concluída também pode envolver sobrecarga, retrabalho ou concentração de tarefas.",
            s["small"],
        )
    )

    # 4 — métricas PSM da equipe
    story.append(p("4 Quê Quem Quando", s["h2"]))
    story.append(
        p(
            "Definam ações para cada tópico priorizado. A ação deve mudar uma prática da equipe e permitir "
            "acompanhamento durante a próxima etapa.",
            s["small"],
        )
    )

    # Métricas oficiais (artigo §3.2.1 / Tabela 1):
    # - Custo e Esforço (Recursos e Custos): desvio e participação
    # - Desempenho dos Processos: densidade e taxa de correção
    # - Calendário e Progresso: conformidade (ICP)
    q4 = [
        [
            p("<b>Código</b>", s["cellb"]),
            p("<b>Ação — O que faremos</b>", s["cellb"]),
            p("<b>Quem acompanhará</b>", s["cellb"]),
            p("<b>Métrica (PSM da equipe)</b>", s["cellb"]),
        ],
        [
            p("C2", s["cell"]),
            p(
                "Reuniões periódicas para planejamento e acompanhamento das tarefas.",
                s["cell"],
            ),
            p("Davi, Mateus", s["cell"]),
            p(
                "<b>Custo e Esforço</b> — Participação percentual "
                "(horas do integrante ÷ horas totais da equipe). "
                "Critério: participação &lt; 10% → redistribuir tarefas.",
                s["cell"],
            ),
        ],
        [
            p("C2", s["cell"]),
            p(
                "Reporte periódico do status e pendências de cada atividade entre pessoas da mesma "
                "dupla e entre duplas, via mensagens.",
                s["cell"],
            ),
            p("Dante, Davi, Karolina", s["cell"]),
            p(
                "<b>Calendário e Progresso</b> — Conformidade / ICP "
                "(tarefas concluídas no prazo ÷ tarefas com prazo até a data) "
                "e lista das tarefas atrasadas. Critério: conformidade &lt; 70% → "
                "redistribuir as atrasadas.",
                s["cell"],
            ),
        ],
        [
            p("C4", s["cell"]),
            p(
                "Após o planejamento semanal, organizar as tarefas em issues para satisfazer a "
                "categoria Calendário e Progresso do PSM.",
                s["cell"],
            ),
            p("Bryan, Pedro", s["cell"]),
            p(
                "<b>Calendário e Progresso</b> — Conformidade / ICP "
                "(tarefas concluídas no prazo ÷ tarefas com prazo até a data). "
                "Critério: conformidade &lt; 70% → redistribuir as tarefas atrasadas. "
                "Fonte: issues/CSV em gestao-psm/.",
                s["cell"],
            ),
        ],
    ]
    tq = Table(q4, colWidths=[1.3 * cm, 6.5 * cm, 3.3 * cm, 5.7 * cm])
    tq.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.4, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.9, 0.9, 0.9)),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(KeepTogether([tq]))
    story.append(Spacer(1, 6))
    story.append(
        p(
            "Usem as métricas definidas pela equipe para Calendário e Progresso, Desempenho do Processo "
            "ou Custo e Esforço, conforme a relação com a ação. Se nenhuma se aplicar, expliquem como "
            "verificarão a execução. Nas próximas semanas, faremos acompanhamento dos projetos a cada aula.",
            s["small"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(
        p(
            "Entreguem um PDF por equipe no moodle e indique aqui o link para o commit no repositório da equipe.",
            s["body"],
        )
    )
    story.append(
        p(
            "<b>Link para o commit no repositório:</b> _____________________________________________",
            s["body"],
        )
    )
    story.append(Spacer(1, 10))
    story.append(
        p(
            "Dinâmicas adaptadas de FunRetrospectives: funretrospectives.com/pt/os-tres-porquinhos/ "
            "e funretrospectives.com/pt/que-quem-quando/.",
            s["footer"],
        )
    )
    story.append(
        p("Qualidade de Software 1 | 2026-2 | Profa. Cristiane Ramos", s["footer"])
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    for path in (OUT, OUT_DOWNLOADS):
        doc = SimpleDocTemplate(
            str(path),
            pagesize=A4,
            leftMargin=1.5 * cm,
            rightMargin=1.5 * cm,
            topMargin=1.2 * cm,
            bottomMargin=1.2 * cm,
            title="Retrospectiva E1 — Betty Snyder",
        )
        doc.build(story)
        print(f"Gerado: {path}")


if __name__ == "__main__":
    build()
