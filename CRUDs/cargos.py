import os
from utils.arquivo_json import ler_json, salvar_json
 
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_CARGOS = "C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\cargos.json"

def criar_cargo():
    print("\n--- CADASTRO DE CARGO ---")

    cargos = ler_json(CAMINHO_CARGOS)

    if cargos:
        novo_id = cargos[-1]["id"] + 1
    else:
        novo_id = 1

    nome = input("Nome do cargo: ")
    salario_base = float(input("Salário base: "))

    cargo = {
        "id": novo_id,
        "nome": nome,
        "salario_base": salario_base,
        "situacao": "Ativo"
    }

    cargos.append(cargo)
    salvar_json(CAMINHO_CARGOS, cargos)

    print("\nCargo cadastrado com sucesso!\n")


def listar_cargos():
    print("\n--- LISTA DE CARGOS ---\n")

    cargos = ler_json(CAMINHO_CARGOS)

    if not cargos:
        print("Nenhum cargo cadastrado.\n")
        return

    for cargo in cargos:
        print(f"ID: {cargo['id']}")
        print(f"Nome: {cargo['nome']}")
        print(f"Salário Base: {cargo['salario_base']}")
        print(f"Situação: {cargo['situacao']}")
        print("-" * 30)

    print()


def buscar_cargo_por_id():
    print("\n--- BUSCAR CARGO POR ID ---\n")

    try:
        id_busca = int(input("Digite o ID do cargo: "))
    except ValueError:
        print("Digite um ID válido.\n")
        return

    cargos = ler_json(CAMINHO_CARGOS)

    for cargo in cargos:
        if cargo["id"] == id_busca:
            print(f"ID: {cargo['id']}")
            print(f"Nome: {cargo['nome']}")
            print(f"Salário Base: {cargo['salario_base']}")
            print(f"Situação: {cargo['situacao']}")
            print()
            return

    print("Cargo não encontrado.\n")


def atualizar_cargo():
    print("\n--- ATUALIZAR CARGO ---\n")

    try:
        id_cargo = int(input("Digite o ID do cargo: "))
    except ValueError:
        print("Digite um ID válido.\n")
        return

    cargos = ler_json(CAMINHO_CARGOS)

    for cargo in cargos:
        if cargo["id"] == id_cargo:
            cargo["nome"] = input("Novo nome do cargo: ")
            cargo["salario_base"] = float(input("Novo salário base: "))

            salvar_json(CAMINHO_CARGOS, cargos)
            print("\nCargo atualizado com sucesso!\n")
            return

    print("Cargo não encontrado.\n")


def remover_cargo():
    print("\n--- REMOVER CARGO ---\n")

    try:
        id_cargo = int(input("Digite o ID do cargo: "))
    except ValueError:
        print("Digite um ID válido.\n")
        return

    cargos = ler_json(CAMINHO_CARGOS)

    for cargo in cargos:
        if cargo["id"] == id_cargo:
            cargos.remove(cargo)
            salvar_json(CAMINHO_CARGOS, cargos)
            print("\nCargo removido com sucesso!\n")
            return

    print("Cargo não encontrado.\n")
