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
