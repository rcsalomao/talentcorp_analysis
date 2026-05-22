import re

MESES = {
    "janeiro": "01",
    "fevereiro": "02",
    "março": "03",
    "abril": "04",
    "maio": "05",
    "junho": "06",
    "julho": "07",
    "agosto": "08",
    "setembro": "09",
    "outubro": "10",
    "novembro": "11",
    "dezembro": "12",
}


def padronizar_nome(nome: str, log: dict):
    if not nome or not isinstance(nome, str):
        log["padronizar_nome"]["nomes_invalidos"].append(nome)
        return None
    nome_padronizado = re.sub(r"\s+", " ", nome.strip().title())
    if nome != nome_padronizado:
        log["padronizar_nome"]["nomes_corrigidos"].append(nome)
    return nome_padronizado


def normalizar_cpf(cpf: str, log: dict):
    if not cpf or not isinstance(cpf, str):
        log["normalizar_cpf"]["cpfs_invalidos"].append(cpf)
        return None
    valid_pat = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")
    if re.match(valid_pat, cpf):
        return cpf
    cpf_nums = re.sub(r"\D", "", cpf)
    if len(cpf_nums) != 11:
        log["normalizar_cpf"]["cpfs_invalidos"].append(cpf)
        return None
    log["normalizar_cpf"]["cpfs_corrigidos"].append(cpf)
    return f"{cpf_nums[0:3]}.{cpf_nums[3:6]}.{cpf_nums[6:9]}-{cpf_nums[9:11]}"


def validar_email(email: str, funcionario: str, log: dict):
    if not email or not isinstance(email, str):
        log["validar_email"]["emails_invalidos"].append((funcionario, email))
        return False
    pat = re.compile(r"^[\w\.-]+@[\w\.-]+\.(com|com\.br|net|org|br)$")
    if re.match(pat, email):
        return True
    else:
        log["validar_email"]["emails_invalidos"].append((funcionario, email))
        return False


def padronizar_cargo(cargo: str):
    if not cargo or not isinstance(cargo, str):
        return None
    return (
        cargo.strip()
        .title()
        .replace(" De ", " de ")
        .replace("Ti", "TI")
        .replace("Rh", "RH")
        .replace("Estagia", "Estagiá")
        .replace("Senior", "Sênior")
        .replace("Plena", "Pleno")
        .replace("Pleno", "Pleno(a)")
        .replace("Desenvolvedora", "Desenvolvedor")
        .replace("Desenvolvedor", "Desenvolvedor(a)")
        .replace("Estagiária", "Estagiário")
        .replace("Estagiário", "Estagiário(a)")
    )


def salario_para_float(salario: str):
    if not salario or not isinstance(salario, str):
        return None
    a = re.sub(r"^R\$\s*", "", salario)
    b = re.sub(r"\.", "", a)
    c = re.sub(r",", ".", b)
    return float(c.strip())


def padronizar_data(data: str, log: dict):
    if not data or not isinstance(data, str):
        log["padronizar_data"]["datas_invalidas"] += 1
        return None
    pat1 = re.compile(r"\d{2}/\d{2}/\d{4}")
    pat2 = re.compile(r"\d{4}-\d{2}-\d{2}")
    if re.match(pat1, data):
        return data
    elif re.match(pat2, data):
        log["padronizar_data"]["datas_convert_AAAA_MM_DD"] += 1
        year, month, date = re.match(r"(\d{4})-(\d{2})-(\d{2})", data).groups()  # type: ignore[union-attr]
        return f"{date}/{month}/{year}"
    else:
        log["padronizar_data"]["datas_convert_formato_extenso"] += 1
        date, month_extenso, year = tuple(data.split(" de "))
        return f"{date.zfill(2)}/{MESES[month_extenso]}/{year}"


def padronizar_regime(regime: str):
    return regime.strip().upper().replace("ESTAGIO", "Estágio")


def classificar_nivel(cargo: str):
    if not cargo or not isinstance(cargo, str):
        return None
    cl = cargo.lower()
    if "estagiár" in cl:
        return "Estagiário"
    elif "gerente" in cl:
        return "Liderança"
    else:
        return "Operacional"


def padronizar_telefone(telefone: str, log: dict):
    if not telefone or not isinstance(telefone, str):
        log["padronizar_telefone"]["telefones_invalidos"] += 1
        return None
    pat = re.compile(r"\(\d{2}\) 9?\d{4}-\d{4}")
    if re.match(pat, telefone):
        return telefone
    else:
        nums = re.sub(r"\D", "", telefone)
        if len(nums) != 11:
            log["padronizar_telefone"]["telefones_invalidos"] += 1
            return None
        log["padronizar_telefone"]["telefones_corrigidos"] += 1
        return f"({nums[0:2]}) {nums[2:-4]}-{nums[-4:]}"
