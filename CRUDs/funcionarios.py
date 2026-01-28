from utils.arquivo_json import ler_json, salvar_json

# CAMINHO_FUNCIONARIOS = "C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\funcionarios.json"
CAMINHO_FUNCIONARIOS = "..\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\funcionarios.json"

# CAMINHO_CARGOS = "C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\cargos.json"
CAMINHO_CARGOS = "..\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\cargos.json"

def escolher_cargo():
    cargos = ler_json(CAMINHO_CARGOS)

    cargos_ativos = [c for c in cargos if c["situacao"] == "Ativo"]

    if not cargos_ativos:
        print("\nNenhum cargo ativo disponível.\n")
        return None

    print("\n--- CARGOS DISPONÍVEIS ---\n")
    for cargo in cargos_ativos:
        print(f"ID: {cargo['id']} | {cargo['nome']} | R$ {cargo['salario_base']}")

    try:
        id_cargo = int(input("\nDigite o ID do cargo: "))
    except ValueError:
        print("ID inválido.")
        return None

    for cargo in cargos_ativos:
        if cargo["id"] == id_cargo:
            return cargo

    print("Cargo não encontrado.")
    return None



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
    
    cargo_escolhido = escolher_cargo()
    if not cargo_escolhido:
        print("\nCadastro cancelado.\n")
        return

    funcionario = {
        "id": novo_id,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "cargo_id": cargo_escolhido["id"],
        "cargo_nome": cargo_escolhido["nome"],
        "salario_base": cargo_escolhido["salario_base"],
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
        print(f"Cargo: {funcionario['cargo_nome']}")
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
            print(f"Cargo atual: {funcionario['cargo_nome']}")
            print(f"Salário base atual: R$ {funcionario['salario_base']}")
            print(f"Situação atual: {funcionario['situacao']}\n")

            novo_nome = input("Novo nome (ENTER para manter): ")
            novo_cpf = input("Novo CPF (ENTER para manter): ")
            novo_telefone = input("Novo telefone (ENTER para manter): ")
            novo_email = input("Novo email (ENTER para manter): ")

            print("\nDeseja alterar o cargo?")
            print("1 - Sim")
            print("2 - Não")
            opcao_cargo = input("Escolha: ")

            nova_situacao = input(
                "Nova situação (Ativo/Inativo) (ENTER para manter): "
            )

            if novo_nome:
                funcionario["nome"] = novo_nome
            if novo_cpf:
                funcionario["cpf"] = int(novo_cpf)
            if novo_telefone:
                funcionario["telefone"] = int(novo_telefone)
            if novo_email:
                funcionario["email"] = novo_email
            if opcao_cargo == "1":
                cargo_escolhido = escolher_cargo()
                if cargo_escolhido:
                    funcionario["cargo_id"] = cargo_escolhido["id"]
                    funcionario["cargo_nome"] = cargo_escolhido["nome"]
                    funcionario["salario_base"] = cargo_escolhido["salario_base"]

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
            print(f"Cargo: {funcionario['cargo_id']}")

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
            print(f"Cargo: {funcionario['cargo_nome']}")
            print(f"Situação: {funcionario['situacao']}\n")
            return

    print("\nFuncionário não encontrado.\n")
