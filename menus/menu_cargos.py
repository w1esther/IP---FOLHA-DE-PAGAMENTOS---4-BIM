from CRUDs.cargos import criar_cargo, listar_cargos, buscar_cargo_por_id, atualizar_cargo, remover_cargo

def menu_cargos():
    while True:
     
        print('\n\n Selecione o número correspondente à operação que deseja realizar com os cargos: \n\n'
              ' - 1 Criar \n\n'
              ' - 2 Listar \n\n'
              ' - 3 Buscar por ID \n\n'
              ' - 4 Remover cargo \n\n'
              ' - 5 Atualizar cargo \n\n'
              ' - 0 Sair do sistema \n\n')

        try:
            opcao_cargos = int(input("Digite a opção: "))
        except ValueError:
            print("\nDigite apenas números!\n")
            continue 

        if opcao_cargos == 1:
            criar_cargo()

        elif opcao_cargos == 2:
            listar_cargos()

        elif opcao_cargos == 3:
            buscar_cargo_por_id()

        elif opcao_cargos == 4:
            remover_cargo()

        elif opcao_cargos == 5:
            atualizar_cargo()

        elif opcao_cargos == 0:
            break
