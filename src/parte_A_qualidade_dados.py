import re


def questao_1(log: dict):
    print(">>> Questão 01: Quantos funcionários tinham e-mail inválido? Quais são eles?")
    print(
        f"Total de funcionários com email inválido: {len(log['validar_email']['emails_invalidos'])}"
    )
    print("Nome dos funcionários:")
    for n, e in log["validar_email"]["emails_invalidos"]:
        print(n)
    print()


def questao_2(log: dict):
    print(">>> Questão 02: Quantos CPFs precisaram de normalização? Liste os formatos encontrados.")
    print(
        f"Total de cpfs que foram corrigidos: {len(log['normalizar_cpf']['cpfs_corrigidos'])}"
    )
    print("Formatos de cpfs incorretos encontrados:")
    for c in log["normalizar_cpf"]["cpfs_corrigidos"]:
        print(c)
    print()


def questao_3(log: dict):
    print(">>> Questão 03: Quantos nomes tinham algum tipo de inconsistência? Quais eram os problemas mais comuns?")
    print(
        f"Total de nomes que foram corrigidos: {len(log['padronizar_nome']['nomes_corrigidos'])}"
    )
    counter = {
        "all_caps": 0,
        "all_mini": 0,
        "extra_inner_spaces": 0,
        "extra_outer_spaces": 0,
    }
    for c in log["padronizar_nome"]["nomes_corrigidos"]:
        if c == c.upper():
            counter["all_caps"] += 1
        if c == c.lower():
            counter["all_mini"] += 1
        if c != c.strip():
            counter["extra_outer_spaces"] += 1
        if c != re.sub("\w\s{2,}\w", "", c):
            counter["extra_inner_spaces"] += 1
    logger = {
        "all_caps": "Total de nomes em maiúsculo: ",
        "all_mini": "Total de nomes em minúsculo: ",
        "extra_inner_spaces": "Total de nomes com espaços em branco externamente: ",
        "extra_outer_spaces": "Total de nomes com espaços em branco internamente: ",
    }
    ordered_counters = dict(
        sorted(counter.items(), key=lambda item: item[1], reverse=True)
    )
    for k, v in ordered_counters.items():
        print(logger[k], v)
    print()
