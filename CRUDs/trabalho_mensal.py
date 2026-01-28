from utils.arquivo_json import ler_json, salvar_json
import os


PASTA_DADOS = '..\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\'
ARQUIVO_TRABALHO = PASTA_DADOS + 'trabalho_mensal.json'

dados_trabalho = {
    "mes": None,
    "ano": None,
    "frequencias": []
}


def carregar_trabalhos():
    if not os.path.exists(ARQUIVO_TRABALHO):
        salvar_json(ARQUIVO_TRABALHO, [])
        return []
    return ler_json(ARQUIVO_TRABALHO)


def salvar_trabalhos(lista):
    salvar_json(ARQUIVO_TRABALHO, lista)



def definir_mes_ano():
    global dados_trabalho

    try:
        mes = int(input("Digite o mês (1-12): "))
        ano = int(input("Digite o ano: "))
        if mes < 1 or mes > 12:
            print("Mês inválido.\n")
            return
    except ValueError:
        print("Dados inválidos.\n")
        return

    trabalhos = carregar_trabalhos()

    for t in trabalhos:
        if t["mes"] == mes and t["ano"] == ano:
            dados_trabalho = t
            print(f"\nMês {mes}/{ano} carregado.\n")
            return

    dados_trabalho = {
        "mes": mes,
        "ano": ano,
        "frequencias": []
    }

    trabalhos.append(dados_trabalho)
    salvar_trabalhos(trabalhos)

    print(f"\nNovo mês {mes}/{ano} criado.\n")




def registrar_frequencia():
    if not dados_trabalho["mes"]:
        print("Defina o mês/ano primeiro.\n")
        return

    funcionarios = ler_json(PASTA_DADOS + "funcionarios.json")

    try:
        id_func = int(input("ID do funcionário: "))
    except ValueError:
        print("ID inválido.\n")
        return

    for f in funcionarios:
        if f["id"] == id_func:
            dias = int(input("Dias trabalhados: "))
            faltas = int(input("Faltas: "))
            horas_extras = int(input("Horas extras: "))

            destino = "NENHUM"
            if horas_extras > 0:
                print("\n1 - Converter em férias")
                print("2 - Receber como remuneração")
                opcao = input("Escolha: ")

                if opcao == "1":
                    destino = "FERIAS"
                elif opcao == "2":
                    destino = "REMUNERACAO"

            dados_trabalho["frequencias"].append({
                "funcionario_id": f["id"],
                "nome": f["nome"],
                "dias_trabalhados": dias,
                "faltas": faltas,
                "horas_extras": horas_extras,
                "destino_horas_extras": destino
            })

            salvar_trabalho_mensal()
            print("\nFrequência registrada.\n")
            return

    print("Funcionário não encontrado.\n")




def atualizar_frequencia():
    try:
        id_func = int(input("ID do funcionário: "))
    except ValueError:
        print("ID inválido.\n")
        return

    for freq in dados_trabalho["frequencias"]:
        if freq["funcionario_id"] == id_func:
            dias = input("Dias trabalhados (ENTER mantém): ")
            faltas = input("Faltas (ENTER mantém): ")
            horas = input("Horas extras (ENTER mantém): ")

            if dias:
                freq["dias_trabalhados"] = int(dias)
            if faltas:
                freq["faltas"] = int(faltas)
            if horas:
                freq["horas_extras"] = int(horas)

            salvar_trabalho_mensal()
            print("\nFrequência atualizada.\n")
            return

    print("Frequência não encontrada.\n")




def listar_frequencias():
    trabalhos = carregar_trabalhos()

    if not trabalhos:
        print("Nenhum mês registrado.\n")
        return

    for t in trabalhos:
        print(f"\n=== {t['mes']:02d}/{t['ano']} ===")

        if not t["frequencias"]:
            print("Nenhuma frequência registrada.")
            continue

        for f in t["frequencias"]:
            print(f"ID: {f['funcionario_id']}")
            print(f"Nome: {f['nome']}")
            print(f"Dias trabalhados: {f['dias_trabalhados']}")
            print(f"Faltas: {f['faltas']}")
            print(f"Horas extras: {f['horas_extras']}")
            print(f"Destino horas extras: {f['destino_horas_extras']}")
            print("-" * 30)




def salvar_trabalho_mensal():
    trabalhos = carregar_trabalhos()

    for i, t in enumerate(trabalhos):
        if t["mes"] == dados_trabalho["mes"] and t["ano"] == dados_trabalho["ano"]:
            trabalhos[i] = dados_trabalho
            break

    salvar_trabalhos(trabalhos)


def carregar_trabalho_mensal():
    global dados_trabalho

    try:
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
    except ValueError:
        print("Dados inválidos.\n")
        return

    trabalhos = carregar_trabalhos()

    for t in trabalhos:
        if t["mes"] == mes and t["ano"] == ano:
            dados_trabalho = t
            print(f"\nMês {mes}/{ano} carregado com sucesso.\n")
            return

    print("Mês/ano não encontrado.\n")