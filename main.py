from src.data_ingestion import get_clean_data
from src.data_writing import write_csv
from src.parte_A_qualidade_dados import questao_1, questao_2, questao_3
from src.parte_B_KPI import (
    get_dataframe,
    questao_4,
    questao_5,
    questao_6,
    questao_7,
    questao_8,
    questao_9,
    questao_10,
)
from src.parte_C_OKR import questao_11, questao_12
from src.parte_D_analise_propostas import questao_13, questao_14, questao_15

data, log = get_clean_data(r"./data/input/funcionarios.json", True)
write_csv(data, r"./data/output/funcionarios_clean.csv")

print("=== QUALIDADE DOS DADOS ===\n")
questao_1(log)
questao_2(log)
questao_3(log)

df = get_dataframe("./data/output/funcionarios_clean.csv")

print("=== ANÁLISE DOS KPIS ===\n")
questao_4(df)
questao_5(df)
questao_6(df)
questao_7(df)
questao_8(df)
questao_9(df)
questao_10(df)

print("=== CONFRONTO COM OKRS ===\n")
questao_11(df)
questao_12(df)

print("=== ANÁLISE E PROSPOSTAS ===\n")
questao_13(df, log)
questao_14(df)
questao_15(df)
