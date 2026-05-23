import pandas as pd


def questao_13(df: pd.DataFrame, log: dict):
    print(
        ">>> Questão 13: Crie pelo menos 2 KPIs que você acha relevantes e que NÃO foram pedidos acima. Justifique cada um."
    )
    print("1º KPI: Quantidade e proporção de funcionários por nível:")
    print(
        "Como se calcula: 'Quantidade de funcionários por nível' / 'Total de funcionários'"
    )
    d = (
        df.groupby(by="nivel")
        .agg(total=("id", "count"))
        .reset_index()
        .sort_values(by="total", ascending=False)
    )
    d["percentual"] = d["total"] / d["total"].sum()
    print(d)
    print()
    print("2º KPI: Taxa média de inconsistências cadastrais:")
    print(
        "Como se calcula: 'Somatório dos dados inconsistentes e inválidos' / 'Quantidade dos tipos de dados avaliados'"
    )
    d = {
        "cpf": sum([len(v) for v in log["normalizar_cpf"].values()]),
        "telefone": sum([v for v in log["padronizar_telefone"].values()]),
        "email": sum([len(v) for v in log["validar_email"].values()]),
        "data": sum([v for v in log["padronizar_data"].values()]),
        "nome": sum([len(v) for v in log["padronizar_nome"].values()]),
    }
    df = pd.DataFrame.from_dict(d, orient="index", columns=["total"])
    df["proporção"] = df["total"] / df["total"].sum() * 100
    # print(df.sort_values(by="total", ascending=False))
    print(f"Valor para este dataset: {df['total'].mean()}")
    print()


def questao_14(df: pd.DataFrame):
    print(
        ">>> Questão 14: Com base nos dados que você encontrou, proponha um novo OKR para o próximo trimestre. Use o formato: Objetivo + pelo menos 2 KRs mensuráveis."
    )
    print("""\
"OKR: Melhoria da qualidade cadastral dos dados da empresa, por meio da redução da 'taxa média de inconsistências cadastraris'."
"Horizonte: Trimestral"
"KPI base: Minimização do 2º KPI (Taxa média de inconsistências cadastrais) apresentado anteriormente. Quanto mais próximo de 0, melhor.""")
    print()


def questao_15(df: pd.DataFrame):
    print(
        ">>> Questão 15: Se você fosse a Vanessa (Gerente de RH), qual seria sua prioridade nos próximos 30 dias? Justifique com dados."
    )
    print("""\
Levando em considerarção as questões anteriores e o curto prazo de 30 dias para a apresentação do relatório e resultados, entendo que o amis interessante seria completar num primeiro momento os objetivos mais fáceis.
Neste primeiro momento creio que é plenamente possível realizar a execução do objetivo O1-OKR1 (zerar as inconsistências cadastrais) e iniciar os objetivos O2-OKR2 (reduzir PJs no TI de 4 para 2) e O2-OKR1 (atingir 70% dos funcionários em regime CLT).
Para o objetivo O1-OKR1, entendo que uma estratégia eficaz consiste em realizar sessões regulares de treinamento e orientação para os funcionários responsáveis pelo registro, além da definição de protocolos e métodos para a execução da tarefa, a fim de minimizar e eliminar o surgimento das inconsistências cadastrais.
Os objetivos O2-OKR1 e O2-OKR2, por sua natureza, são convergentes e portante a realização de um também implica na realização do outro.
A redução de PJs de 4 para 2 também provocará o aumento na proporção de funcionários CLT.
Creio que a dificuldade possa residir na negociação entre os respectivos funcionários e aí se encontra a incerteza sobre o prazo de execução destes objetivos.
Além destes 3 objetivos discutidos, há de se ter em mente o objetivo O3-OKR1 (redução de custo do Comercial em 15%) que envolve os respectivos funcionários e as partes responsáveis pela tomada de decisão sobre o tema e, portanto, entendo que este objetivo é o mais delicado e incerto quanto sua exequibilidade e prazo.""")
    print()
