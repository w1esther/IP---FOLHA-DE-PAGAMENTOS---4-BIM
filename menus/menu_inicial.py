from menus.menu_funcionarios import menu_funcionarios
from menus.menu_cargos import menu_cargos
from menus.menu_trabalho_mensal import menu_trabalho_mensal
from menus.menu_relatorios import menu_relatorios
from menus.menu_salarios import menu_salarios

def menu_inicial():
    while True:
        print("""
        === SISTEMA DE FOLHA DE PAGAMENTO ===

        1 - CRUD de Funcionários
        2 - CRUD de Cargos
        3 - Trabalho Mensal
        4 - Cálculo de Salário
        5 - Relatórios
        0 - Sair
        """)

        try:
            opcao = int(input("Digite a opção: "))
        except ValueError:
            print("\nDigite apenas números!\n")
            continue

        if opcao == 1:
            menu_funcionarios()

        elif opcao == 2:
            menu_cargos()

        elif opcao == 3:
            menu_trabalho_mensal()

        elif opcao == 4:
            menu_salarios()

        elif opcao == 5:
            menu_relatorios()

        elif opcao == 0:
            print("\nEncerrando o sistema...\n")
            break

        else:
            print("\nOpção inválida!\n")