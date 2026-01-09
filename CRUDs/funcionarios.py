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



def atualizar_funcionario():
    print("\n--- ATUALIZAR FUNCIONÁRIO ---\n")

    funcionarios = ler_json(CAMINHO_FUNCIONARIOS)

    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return

    try:
        id_busca = int(input("Digite o ID do funcionário: "))
    except ValueError:
        print("\nID inválido.\n")
        return

    for funcionario in funcionarios:
        if funcionario["id"] == id_busca:

            print("\nFuncionário encontrado:")
            print(f"Nome atual: {funcionario['nome']}")
            print(f"CPF atual: {funcionario['cpf']}")
            print(f"Telefone atual: {funcionario['telefone']}")
            print(f"Email atual: {funcionario['email']}")
            print(f"Cargo atual: {funcionario['cargo']}")
            print(f"Situação atual: {funcionario['situacao']}\n")

            novo_nome = input("Novo nome (ENTER para manter): ")
            novo_cpf = input("Novo CPF (ENTER para manter): ")
            novo_telefone = input("Novo telefone (ENTER para manter): ")
            novo_email = input("Novo email (ENTER para manter): ")
            novo_cargo = input("Novo cargo (ENTER para manter): ")
            nova_situacao = input("Nova situação (Ativo/Inativo) (ENTER para manter): ")

            if novo_nome:
                funcionario["nome"] = novo_nome
            if novo_cpf:
                funcionario["cpf"] = int(novo_cpf)
            if novo_telefone:
                funcionario["telefone"] = int(novo_telefone)
            if novo_email:
                funcionario["email"] = novo_email
            if novo_cargo:
                funcionario["cargo"] = novo_cargo
            if nova_situacao:
                funcionario["situacao"] = nova_situacao

            salvar_json(CAMINHO_FUNCIONARIOS, funcionarios)

            print("\nFuncionário atualizado com sucesso!\n")
            return

    print("\nFuncionário não encontrado.\n")



def remover_funcionario():
    print("\n--- REMOVER FUNCIONÁRIO ---\n")

    funcionarios = ler_json(CAMINHO_FUNCIONARIOS)

    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return

    try:
        id_busca = int(input("Digite o ID do funcionário que deseja remover: "))
    except ValueError:
        print("\nID inválido.\n")
        return

    for funcionario in funcionarios:
        if funcionario["id"] == id_busca:

            print("\nFuncionário encontrado:")
            print(f"ID: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")

            confirmacao = input(
                "\nTem certeza que deseja REMOVER DEFINITIVAMENTE? (S/N): "
            ).upper()

            if confirmacao == "S":
                funcionarios.remove(funcionario)
                salvar_json(CAMINHO_FUNCIONARIOS, funcionarios)
                print("\nFuncionário removido com sucesso!\n")
            else:
                print("\nRemoção cancelada.\n")

            return

    print("\nFuncionário não encontrado.\n")



def buscar_funcionario_por_id():
    print("\n--- BUSCAR FUNCIONÁRIO POR ID ---\n")

    funcionarios = ler_json(CAMINHO_FUNCIONARIOS)

    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return

    try:
        id_busca = int(input("Digite o ID do funcionário: "))
    except ValueError:
        print("\nID inválido.\n")
        return

    for funcionario in funcionarios:
        if funcionario["id"] == id_busca:
            print("\nFuncionário encontrado:\n")
            print(f"ID: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"CPF: {funcionario['cpf']}")
            print(f"Telefone: {funcionario['telefone']}")
            print(f"Email: {funcionario['email']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Situação: {funcionario['situacao']}\n")
            return

    print("\nFuncionário não encontrado.\n")
