from CRUDs.funcionarios import criar_funcionario, listar_funcionarios, atualizar_funcionario, remover_funcionario, buscar_funcionario_por_id

def menu_funcionarios():
    while True:
     
        print('\n\n Selecione o número correspondente à operação que deseja realizar com os funcionários: \n\n - 1 Criar \n\n - 2 Listar \n\n - 3 Atualizar \n\n - 4 Remover \n\n - 5 Buscar por ID \n\n - 0 Sair do sistema \n\n')

        try:
            opcao_funcionarios = int(input("Digite a opção: "))
        except ValueError:
            print("\nDigite apenas números!\n")
            continue 

        if opcao_funcionarios == 1:
            criar_funcionario()

        if opcao_funcionarios == 2:
            listar_funcionarios()

        if opcao_funcionarios == 3:
            atualizar_funcionario()

        if opcao_funcionarios == 4:
            remover_funcionario()

        if opcao_funcionarios == 5:
            buscar_funcionario_por_id()
        
        if opcao_funcionarios == 0:
            break
        