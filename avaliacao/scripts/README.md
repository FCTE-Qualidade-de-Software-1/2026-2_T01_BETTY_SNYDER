# Scripts de coleta e consolidação

Scripts que transformam dados brutos em consolidados ou automatizam a coleta instrumentada (ex.: desempenho).

Convenções:

- Nome do script alinhado à métrica ou ao cenário (`coletar_T_ini_coldstart.py`, `consolidar_M-INT_tarefas.py`).
- Cada script documenta, no cabeçalho, entrada (`dados/.../bruto/`), saída (`dados/.../consolidado/`) e métricas GQM afetadas.
- Não gravar caminhos com nomes reais de participantes; usar apenas códigos (PA/PB) ou IDs de execução de laboratório.

Enquanto não houver scripts versionados, esta pasta permanece com `.gitkeep`.
