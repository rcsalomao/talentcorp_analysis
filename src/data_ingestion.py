import utils.functions as uf
import json


def get_clean_data(data_filename: str, print_log_limpeza: bool = True):
    with open(data_filename, "r", encoding="utf-8") as f:
        funcionarios = json.load(f)

    # Idealmente não se deve atribuir funções lambda.
    # Não é para isso que elas foram feitas.
    padronizar_estado_civil = (  # noqa: E731
        lambda ec: None
        if not ec or not isinstance(ec, str)
        else ec.strip()
        .title()
        .replace("Casada", "Casado")
        .replace("Casado", "Casado(a)")
        .replace("Solteira", "Solteiro")
        .replace("Solteiro", "Solteiro(a)")
        .replace("Divorciada", "Divorciado")
        .replace("Divorciado", "Divorciado(a)")
    )
    formatar_salario = (  # noqa: E731
        lambda v: None
        if not v or not isinstance(v, float)
        else f"R$ {v:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")
    )

    log: dict = {
        "normalizar_cpf": {"cpfs_corrigidos": [], "cpfs_invalidos": []},
        "padronizar_telefone": {"telefones_corrigidos": 0, "telefones_invalidos": 0},
        "validar_email": {
            "emails_invalidos": [],
        },
        "padronizar_data": {
            "datas_invalidas": 0,
            "datas_convert_AAAA_MM_DD": 0,
            "datas_convert_formato_extenso": 0,
        },
        "padronizar_nome": {"nomes_corrigidos": [], "nomes_invalidos": []},
    }

    for f in funcionarios:
        # Padronização dos nomes:
        f["nome"] = uf.padronizar_nome(f["nome"], log)
        # Normalização dos cpfs:
        f["cpf"] = uf.normalizar_cpf(f["cpf"], log)
        # Normalização dos cpfs:
        f["email_valido"] = uf.validar_email(f["email"], f["nome"], log)
        # Padronização dos cargos:
        f["cargo"] = uf.padronizar_cargo(f["cargo"])
        # Padronização dos estados civis:
        f["estado_civil"] = padronizar_estado_civil(f["estado_civil"])
        # Conversão dos salários para float:
        f["salario_num"] = uf.salario_para_float(f["salario"])
        if f["salario_num"] is None:
            f["salario"] = None
        # Padronização das datas de admissão:
        f["data_admissao"] = uf.padronizar_data(f["data_admissao"], log)
        # Padronização dos regimes:
        f["regime"] = uf.padronizar_regime(f["regime"])
        # Classificação de nível:
        f["nivel"] = uf.classificar_nivel(f["cargo"])
        # Padronização dos telefones:
        f["telefone"] = uf.padronizar_telefone(f["telefone"], log)

    if print_log_limpeza:
        print(f"""
{" Relatório de Limpeza ".upper().center(28, "=")}
Total de funcionários: {len(funcionarios)}
Emails inválidos: {len(log["validar_email"]["emails_invalidos"])}
CPFs que precisaram de regularização: {len(log["normalizar_cpf"]["cpfs_corrigidos"])}
Datas convertidas de AAAA-MM-DD: {log["padronizar_data"]["datas_convert_AAAA_MM_DD"]}
Datas convertidas de AAAA-MM-DD: {log["padronizar_data"]["datas_convert_formato_extenso"]}
Telefones inválidos: {log["padronizar_telefone"]["telefones_invalidos"]}
Telefones corrigidos: {log["padronizar_telefone"]["telefones_corrigidos"]}
              """)

    return (funcionarios, log)
