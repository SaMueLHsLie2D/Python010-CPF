
def validar_nome(nome: str) -> bool:
    return bool(nome.strip())


def validar_cpf(cpf: str) -> bool:
    return cpf.isdigit() and len(cpf) == 11


def validar_idade(idade: int) -> bool:
    return 0 <= idade <= 120
