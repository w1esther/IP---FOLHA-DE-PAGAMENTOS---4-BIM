from CRUDs.relatorios import gerar_relatorio_salarios

def menu_relatorios():
    while True:
        print('\n\n Selecione o número correspondente à operação que deseja realizar com os relatórios: z\n\n - 1 Gerar relatório de pagamento dos salários \n\n  - 0 Sair do sistema \n\n')

        try:
            opcao_relatorios = int(input("Digite a opção: "))
        except ValueError:
            print("\nDigite apenas números!\n")
            continue

        if opcao_relatorios == 1:
            gerar_relatorio_salarios()

        elif opcao_relatorios == 0:
            break

