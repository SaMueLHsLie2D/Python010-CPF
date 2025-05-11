
from validador import validar_nome, validar_cpf, validar_idade


def main():
    nome = input("Digite seu nome: ")
    if not validar_nome(nome):
        print("Erro: o nome não pode ser vazio.")
        return

    cpf = input("Digite seu CPF (apenas números): ")
    if not validar_cpf(cpf):
        print("Erro: CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
        return

    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Erro: a idade deve ser um número inteiro.")
        return

    if not validar_idade(idade):
        print("Erro: idade inválida. Deve estar entre 0 e 120.")
        return

    print("\n--- Dados Informados ---")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Idade: {idade}")


if __name__ == "__main__":
    main()
