from utils.arquivo_json import ler_json, salvar_json
import os

PASTA_DADOS = "..\\IP---FOLHA-DE-PAGAMENTOS---4-BIM\\dados\\"
CAMINHO_SALARIOS = PASTA_DADOS + "salarios.json"
CAMINHO_RELATORIOS = PASTA_DADOS + "relatorios_salarios.json"

def gerar_relatorio_salarios():
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
        print("Nenhum salário calculado ainda.\n")
        return

    salarios_gerais = ler_json(CAMINHO_SALARIOS)

    for registro in salarios_gerais:
        if registro["mes"] == mes and registro["ano"] == ano:
            salarios = registro["salarios"]

            if not salarios:
                print("Nenhum salário para esse mês.\n")
                return

            total_pago = sum(s["salario_final"] for s in salarios)
            total_funcionarios = len(salarios)
            media_salarial = total_pago / total_funcionarios

            relatorio = {
                "mes": mes,
                "ano": ano,
                "total_funcionarios": total_funcionarios,
                "total_pago": round(total_pago, 2),
                "media_salarial": round(media_salarial, 2),
                "salarios": [
                    {
                        "funcionario_id": s["funcionario_id"],
                        "nome": s["nome"],
                        "salario_final": s["salario_final"]
                    }
                    for s in salarios
                ]
            }

            if not os.path.exists(CAMINHO_RELATORIOS):
                salvar_json(CAMINHO_RELATORIOS, [relatorio])
            else:
                relatorios = ler_json(CAMINHO_RELATORIOS)

                for r in relatorios:
                    if r["mes"] == mes and r["ano"] == ano:
                        r.update(relatorio)
                        break
                else:
                    relatorios.append(relatorio)

                salvar_json(CAMINHO_RELATORIOS, relatorios)

            print(f"\nRelatório de {mes:02d}/{ano} gerado com sucesso!\n")
            return

    print("Salários não encontrados para esse mês/ano.\n")
