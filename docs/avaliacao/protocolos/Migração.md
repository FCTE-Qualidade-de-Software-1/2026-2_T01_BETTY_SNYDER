# Protocolo de Migração – Flexibilidade (Q3)

## Cenários

- **M1 – Arquivo .apkg**: exportação da coleção com agendamento e mídia, importação em máquina de outro SO.
- **M2 – AnkiWeb**: sincronização da coleção via AnkiWeb entre duas máquinas de SOs diferentes.

## Pré-requisitos

- Coleção padrão (E2-20) disponível e íntegra.
- Script `scripts/verificar_integridade.py` copiado para as duas máquinas.
- Anki Desktop 26.09.3 instalado nas duas máquinas (SOs distintos).
- Conexão com a internet (para M2).

## Procedimento M1 – Arquivo .apkg

1. **Na máquina de origem**:
   - Abrir o Anki Desktop.
   - Selecionar o baralho da coleção padrão.
   - Exportar com as opções: “Incluir agendamento” e “Incluir mídia”.
   - Salvar o arquivo `export_m1.apkg`.
   - Registrar o horário de início da exportação (`T_inicio_export`).

2. **Transferir** o `export_m1.apkg` para a máquina de destino (pendrive, rede, etc.).

3. **Na máquina de destino**:
   - Abrir o Anki Desktop (com uma coleção vazia ou limpa).
   - Importar o `export_m1.apkg`.
   - Registrar o horário de término da importação (`T_fim_import`).

4. **Verificação de integridade**:
   - Na máquina de destino, executar:
     ```bash
     python scripts/verificar_integridade.py --antes /caminho/para/colecao_origem --depois /caminho/para/colecao_destino --saida diff_m1.csv