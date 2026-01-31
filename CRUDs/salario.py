from utils.arquivo_json import ler_json, salvar_json
import os

PASTA_DADOS = "..\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\"
CAMINHO_SALARIOS = PASTA_DADOS + "salarios.json"

def calcular_salarios_mes():
    try:
        mes = int(input("Digite o mês (1-12): "))
        ano = int(input("Digite o ano: "))
        if mes < 1 or mes > 12:
            print("Mês inválido.\n")
            return
    except ValueError:
        print("Dados inválidos.\n")
        return

    funcionarios = ler_json(PASTA_DADOS + "funcionarios.json")
    trabalhos = ler_json(PASTA_DADOS + "trabalho_mensal.json")

    if not os.path.exists(CAMINHO_SALARIOS):
        salvar_json(CAMINHO_SALARIOS, [])

    salarios_gerais = ler_json(CAMINHO_SALARIOS)

    trabalho_mes = None
    for t in trabalhos:
        if t["mes"] == mes and t["ano"] == ano:
            trabalho_mes = t
            break

    if not trabalho_mes:
        print("Mês/ano não encontrado.\n")
        return

    salarios_mes = []

    for freq in trabalho_mes["frequencias"]:
        funcionario = next(
            (f for f in funcionarios if f["id"] == freq["funcionario_id"]),
            None
        )

        if not funcionario or funcionario["situacao"] != "Ativo":
            continue

        salario_base = funcionario["salario_base"]

        desconto_faltas = (salario_base / 30) * freq["faltas"]

        valor_hora = salario_base / 220
        valor_horas_extras = 0

        if freq["horas_extras"] > 0 and freq["destino_horas_extras"] == "REMUNERACAO":
            valor_horas_extras = freq["horas_extras"] * valor_hora * 1.5

        salario_final = salario_base - desconto_faltas + valor_horas_extras

        salarios_mes.append({
            "funcionario_id": funcionario["id"],
            "nome": funcionario["nome"],
            "salario_base": salario_base,
            "desconto_faltas": round(desconto_faltas, 2),
            "valor_horas_extras": round(valor_horas_extras, 2),
            "salario_final": round(salario_final, 2)
        })

    for registro in salarios_gerais:
        if registro["mes"] == mes and registro["ano"] == ano:
            registro["salarios"] = salarios_mes
            break
    else:
        salarios_gerais.append({
            "mes": mes,
            "ano": ano,
            "salarios": salarios_mes
        })

    salvar_json(CAMINHO_SALARIOS, salarios_gerais)
    print(f"\nSalários de {mes:02d}/{ano} calculados com sucesso!\n")




def listar_salarios_mes():
    try:
        mes = int(input("Digite o mês (1-12): "))
        ano = int(input("Digite o ano: "))
        if mes < 1 or mes > 12:
            print("Mês inválido.\n")
            return
    except ValueError:
        print("Dados inválidos.\n")
        return

    if not os.path.exists(CAMINHO_SALARIOS):
        print("Nenhum salário registrado.\n")
        return

    salarios_gerais = ler_json(CAMINHO_SALARIOS)

    for registro in salarios_gerais:
        if registro["mes"] == mes and registro["ano"] == ano:
            print(f"\n--- SALÁRIOS {mes:02d}/{ano} ---\n")

            if not registro["salarios"]:
                print("Nenhum salário calculado para este mês.\n")
                return

            for s in registro["salarios"]:
                print(f"ID Funcionário: {s['funcionario_id']}")
                print(f"Nome: {s['nome']}")
                print(f"Salário Base: R$ {s['salario_base']:.2f}")
                print(f"Desconto por faltas: R$ {s['desconto_faltas']:.2f}")
                print(f"Valor horas extras: R$ {s['valor_horas_extras']:.2f}")
                print(f"Salário final: R$ {s['salario_final']:.2f}")
                print("-" * 30)

            return

    print("\nNenhum salário encontrado para esse mês e ano.\n")
