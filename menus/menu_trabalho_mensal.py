from CRUDs.trabalho_mensal import definir_mes_ano, registrar_frequencia, atualizar_frequencia, listar_frequencias, salvar_trabalho_mensal, carregar_trabalho_mensal

def menu_trabalho_mensal():
    while True:
        print("""
--- MENU TRABALHO MENSAL ---

1 - Definir mês/ano
2 - Registrar frequência
3 - Atualizar frequência
4 - Listar frequências
5 - Salvar dados do mês
6 - Carregar mês anterior
0 - Voltar
""")

        opcao = input("Escolha: ")

        if opcao == "1":
            definir_mes_ano()
        elif opcao == "2":
            registrar_frequencia()
        elif opcao == "3":
            atualizar_frequencia()
        elif opcao == "4":
            listar_frequencias()
        elif opcao == "5":
            salvar_trabalho_mensal()
        elif opcao == "6":
            carregar_trabalho_mensal()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.\n")