from utils.arquivo_json import ler_json, salvar_json

CAMINHO_FUNCIONARIOS = "C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\funcionarios.json"

def criar_funcionario():
    print("\n--- CADASTRO DE FUNCIONÁRIO ---")

    funcionarios = ler_json(CAMINHO_FUNCIONARIOS)

    if funcionarios:
        novo_id = funcionarios[-1]["id"] + 1
    else:
        novo_id = 1

    nome = input("Nome completo: ")
    cpf = int(input("CPF: "))
    telefone = int(input("Telefone: "))
    email = input("Email: ")
    cargo = input("Cargo: ")

    funcionario = {
        "id": novo_id,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "cargo": cargo,
        "situacao": "Ativo"
    }

    funcionarios.append(funcionario)
    salvar_json(CAMINHO_FUNCIONARIOS, funcionarios)

    print("\nFuncionário cadastrado com sucesso!\n")

def listar_funcionarios():

    print("\n--- LISTA DE FUNCIONÁRIOS ---\n")

    funcionarios = ler_json(CAMINHO_FUNCIONARIOS)

    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return

    for funcionario in funcionarios:
        print(f"ID: {funcionario['id']}")
        print(f"Nome: {funcionario['nome']}")
        print(f"CPF: {funcionario['cpf']}")
        print(f"Telefone: {funcionario['telefone']}")
        print(f"Email: {funcionario['email']}")
        print(f"Cargo: {funcionario['cargo']}")
        print(f"Situação: {funcionario['situacao']}")
        print("-" * 30)

    print()
