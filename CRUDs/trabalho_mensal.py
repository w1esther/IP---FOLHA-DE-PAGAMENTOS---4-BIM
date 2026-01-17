from utils.arquivo_json import ler_json, salvar_json

PASTA_DADOS = 'C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\'

dados_trabalho = {
    "mes": None,
    "ano": None,
    "frequencias": []
}

def definir_mes_ano():
    try:
        mes = int(input("Digite o mês (1-12): "))
        ano = int(input("Digite o ano: "))
    except ValueError:
        print("Dados inválidos.")
        return

    nome_arquivo = f"trabalho_{mes:02d}_{ano}.json"
    caminho = PASTA_DADOS + nome_arquivo

    global dados_trabalho

    try:
        dados_trabalho = ler_json(caminho)
        print(f"\nMês {mes}/{ano} carregado com dados existentes.\n")

    except FileNotFoundError:
        dados_trabalho = {
            "mes": mes,
            "ano": ano,
            "frequencias": []
        }
        print(f"\nNovo mês criado: {mes}/{ano}\n")



def registrar_frequencia():
    if not dados_trabalho["mes"]:
        print("Defina o mês/ano primeiro.\n")
        return

    funcionarios = ler_json("C:\\Users\\w1mar\\OneDrive\\Documentos\\GitHub\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\funcionarios.json")

    try:
        id_func = int(input("ID do funcionário: "))
    except ValueError:
        print("ID inválido.")
        return

    for f in funcionarios:
        if f["id"] == id_func:
            dias = int(input("Dias trabalhados: "))
            faltas = int(input("Faltas: "))
            horas_extras = int(input("Horas extras: "))

            destino = "NENHUM"
            if horas_extras > 0:
                print("\nComo deseja utilizar as horas extras?")
                print("1 - Converter em férias (banco de horas)")
                print("2 - Receber como remuneração adicional")

                opcao = input("Escolha: ")

                if opcao == "1":
                    destino = "FERIAS"
                elif opcao == "2":
                    destino = "REMUNERACAO"
                else:
                    print("Opção inválida. Definido como NÃO CONVERTIDO.")

            dados_trabalho["frequencias"].append({
                "funcionario_id": f["id"],
                "nome": f["nome"],
                "dias_trabalhados": dias,
                "faltas": faltas,
                "horas_extras": horas_extras,
                "destino_horas_extras": destino
            })

            print("\nFrequência registrada.\n")
            return

    print("Funcionário não encontrado.\n")



def atualizar_frequencia():
    try:
        id_func = int(input("ID do funcionário: "))
    except ValueError:
        print("ID inválido.")
        return

    for freq in dados_trabalho["frequencias"]:
        if freq["funcionario_id"] == id_func:
            dias = input("Novos dias trabalhados (ENTER mantém): ")
            faltas = input("Novas faltas (ENTER mantém): ")
            horas = input("Novas horas extras (ENTER mantém): ")

            if dias:
                freq["dias_trabalhados"] = int(dias)
            if faltas:
                freq["faltas"] = int(faltas)
            if horas:
                freq["horas_extras"] = int(horas)

                if int(horas) > 0:
                    print("\nDestino das horas extras:")
                    print("1 - Férias")
                    print("2 - Remuneração adicional")
                    opcao = input("Escolha: ")

                    if opcao == "1":
                        freq["destino_horas_extras"] = "FERIAS"
                    elif opcao == "2":
                        freq["destino_horas_extras"] = "REMUNERACAO"
                else:
                    freq["destino_horas_extras"] = "NENHUM"

            print("\nFrequência atualizada.\n")
            return

    print("Frequência não encontrada.\n")



def listar_frequencias():
    if not dados_trabalho["frequencias"]:
        print("Nenhuma frequência registrada.\n")
        return

    print(f"\n--- FREQUÊNCIA {dados_trabalho['mes']}/{dados_trabalho['ano']} ---\n")

    for f in dados_trabalho["frequencias"]:
        print(f"ID: {f['funcionario_id']}")
        print(f"Nome: {f['nome']}")
        print(f"Dias trabalhados: {f['dias_trabalhados']}")
        print(f"Faltas: {f['faltas']}")
        print(f"Horas extras: {f['horas_extras']}")
        print(f"Destino das horas extras: {f['destino_horas_extras']}")
        print("-" * 30)



def salvar_trabalho_mensal():
    if not dados_trabalho["mes"]:
        print("Nada para salvar.\n")
        return

    nome_arquivo = f"trabalho_{dados_trabalho['mes']:02d}_{dados_trabalho['ano']}.json"
    caminho = PASTA_DADOS + nome_arquivo

    salvar_json(caminho, dados_trabalho)
    print(f"\nDados salvos em {nome_arquivo}\n")



def carregar_trabalho_mensal():
    nome = input("Digite o nome do arquivo (ex: trabalho_01_2026.json): ")
    caminho = PASTA_DADOS + nome

    try:
        dados = ler_json(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado.\n")
        return

    global dados_trabalho
    dados_trabalho = dados

    print("\nDados do mês carregados.\n")
