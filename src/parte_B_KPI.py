import pandas as pd
from datetime import datetime as dt


def get_dataframe(file_name: str):
    with open(file_name, "r", encoding="utf-8-sig") as f:
        df = pd.read_csv(f)
    return df


def questao_4(df: pd.DataFrame):
    print(">>> Questão 04: Qual o salário médio por cargo?")
    print("O salário médio por cargo é descrito na seguinte tabela:")
    print(
        df.groupby("cargo")
        .agg(salario_medio=("salario_num", "mean"))
        .reset_index()
        .sort_values(by="salario_medio", ascending=False)
    )
    print()


def questao_5(df: pd.DataFrame):
    print(">>> Questão 05: Qual o salário médio por departamento?")
    print("O salário médio por departamento é descrito na seguinte tabela:")
    print(
        df.groupby("departamento")
        .agg(salario_medio=("salario_num", "mean"))
        .reset_index()
        .sort_values(by="salario_medio", ascending=False)
    )
    print()


def questao_6(df: pd.DataFrame):
    print(">>> Questão 06: Qual departamento tem a maior folha salarial total?")
    print("A folha salarial total por departamento é descrita na seguinte tabela:")
    print(
        df.groupby("departamento")
        .agg(total=("salario_num", "sum"))
        .reset_index()
        .sort_values(by="total", ascending=False)
    )
    print()


def questao_7(df: pd.DataFrame):
    print(">>> Questão 07: Quantos funcionários por regime? Qual o percentual de cada um?")
    print("A quantidade de funcionários por regime é descrita na seguinte tabela:")
    df = df.groupby("regime").agg(total=("id", "count")).reset_index()
    df["percentual"] = df["total"] / df["total"].sum()
    print(df)
    print()


def questao_8(df: pd.DataFrame):
    print(">>> Questão 08: Qual o funcionário com maior tempo de casa? (data de admissão mais antiga)")
    print("O tempo de permanência de cada funcionário é descrito na seguinte tabela:")
    df = df.copy()
    df["tempo_permanencia"] = dt.now() - pd.to_datetime(
        df["data_admissao"], format="%d/%m/%Y"
    )
    print(
        df[["nome", "tempo_permanencia", "departamento"]].sort_values(
            by="tempo_permanencia", ascending=False
        )
    )
    print()


def questao_9(df: pd.DataFrame):
    print(">>> Questão 09: Quantos funcionários por departamento?")
    print(
        "A quantidade de funcionários por departamento é descrita na seguinte tabela:"
    )
    print(
        df.groupby("departamento")
        .agg(total=("id", "count"))
        .reset_index()
        .sort_values(by="total", ascending=False)
    )
    print()


def questao_10(df: pd.DataFrame):
    print(">>> Questão 10: Qual cargo tem mais funcionários?")
    print("A quantidade de funcionários por cargo é descrita na seguinte tabela:")
    print(
        df.groupby("cargo")
        .agg(total=("id", "count"))
        .reset_index()
        .sort_values(by="total", ascending=False)
    )
    print()
