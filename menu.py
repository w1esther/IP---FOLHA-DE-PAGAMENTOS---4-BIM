    
while True:
    print('\n\n Seja bem-vindo(a) ao sistema de folhas de pagamentos!!!  \n\n Selecione em que área deseja realizar a operação e digite o número correspondenrete: \n\n - 1 CRUD de funcionários \n\n - 2 CRUD de cargos \n\n - 3 CRUD de trabalho mensal \n\n - 4 Cálculo de Salário \n\n - 5 Relatório \n\n - 0 Sair do sistema \n\n')

    opcao_inicial = int(input('Digite a opção selecionada: '))

    if opcao_inicial == 1: 

        print('\n\n Selecione o número correspondente à operação que deseja realizar com os funcionários: \n\n - 1 Criar \n\n - 2 Listar \n\n - 3 Atualizar \n\n - 4 Remover \n\n - 0 Sair do sistema \n\n')

        opcao_funcionarios = int(input('Digite a operação desejada: '))

    elif opcao_inicial == 2: 

        print('\n\n Selecione o número correspondente à operação que deseja realizar com os cargos: \n\n - 1 Criar \n\n - 2 Listar \n\n - 3 Atualizar \n\n - 4 Remover \n\n - 0 Sair do sistema \n\n')

        opcao_cargos = int(input('Digite a operação desejada: '))

    elif opcao_inicial == 3:

        print('\n\n Selecione o número correspondente à operação que deseja realizar com os Trabalho mensal de um funcionário: \n\n - 1 Criar \n\n - 2 Listar \n\n - 3 Atualizar \n\n - 4 Remover \n\n - 0 Sair do sistema \n\n')

        opcao_trabalho_mensal = int(input('Digite a operação desejada: '))

    elif opcao_inicial == 4:

        print('\n\n Selecione o número correspondente à operação que deseja realizar com os salários: z\n\n - 1 Calcular salário líquido  \n\n - 2 Calcular salário bruto \n\n - 3 Calcular descontos  \n\n - 4 Calcular acrécimos \n\n - 0 Sair do sistema \n\n')

        opcao_salario = int(input('Digite a operação desejad0: '))

    elif opcao_inicial == 5:

        print('\n\n Selecione o número correspondente à operação que deseja realizar com os relatórios: z\n\n - 1 Gerar relatório de pagamento anual dos salários \n\n - 2 Gerar relatório de pagamento de determinado mês \n\n - 3 Gerar relatório de pagamento de determinado funcionário \n\n - 0 Sair do sistema \n\n')

        opcao_relatorio = int(input('Digite a operação desejada: '))

    elif opcao_inicial == 0:

        break
    
    else: 

        print('\n\n OPERAÇÃO INVÁLIDA! TENTE NOVAMENTE \n\n ')
