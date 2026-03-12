agenda = {}

while True:
    print("\n--- AGENDA TELEFÔNICA ---")
    print("1 - Cadastrar contato")
    print("2 - Buscar contato")
    print("3 - Excluir contato")
    print("4 - Listar contatos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")

        if nome in agenda:
            print("Contato já existe. Telefone será atualizado.")
        
        agenda[nome] = telefone
        print("Contato salvo com sucesso.")

    elif opcao == "2":
        nome = input("Digite o nome do contato para buscar: ")

        if nome in agenda:
            print("Telefone:", agenda[nome])
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome do contato para excluir: ")

        if nome in agenda:
            del agenda[nome]
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        if len(agenda) == 0:
            print("Agenda vazia.")
        else:
            print("\n--- Lista de Contatos ---")
            for nome, telefone in agenda.items():
                print("Nome:", nome, "- Telefone:", telefone)

    elif opcao == "5":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida.")