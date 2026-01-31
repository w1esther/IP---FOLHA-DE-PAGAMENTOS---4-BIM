from CRUDs.salario import calcular_salarios_mes, listar_salarios_mes

def menu_salarios():
    while True:
        print('\n\n Selecione o número correspondente à operação que deseja realizar com os salários: z\n\n - 1 Calcular Salário \n\n - 2 Listar Salários por mês/ano  \n\n - 0  Sair do Sistema \n\n')

        try:
            opcao_salario = int(input("Digite a opção: "))
        except ValueError:
            print("\nDigite apenas números!\n")
            continue

        if opcao_salario == 1:
            calcular_salarios_mes()

        elif opcao_salario == 2:
            listar_salarios_mes()

        elif opcao_salario == 0:
            break