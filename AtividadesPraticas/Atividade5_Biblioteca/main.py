from livro import Livro, LivroDigital
from usuario import Usuario
from biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:

    print("\n===== SISTEMA BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuário")
    print("3 - Realizar empréstimo")
    print("4 - Devolver livro")
    print("5 - Listar livros disponíveis")
    print("6 - Listar livros emprestados")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:

        case "1":
            tipo = input("Livro digital? (s/n): ")

            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")

            if tipo == "s":
                tamanho = float(input("Tamanho do arquivo (MB): "))
                livro = LivroDigital(titulo, autor, ano, tamanho)
            else:
                livro = Livro(titulo, autor, ano)

            biblioteca.adicionar_livro(livro)
            print("Livro cadastrado.")

        case "2":
            nome = input("Nome: ")
            matricula = input("Matrícula: ")

            usuario = Usuario(nome, matricula)
            biblioteca.cadastrar_usuario(usuario)

            print("Usuário cadastrado.")

        case "3":
            nome = input("Nome do usuário: ")
            titulo = input("Título do livro: ")

            usuario = None
            livro = None

            for u in biblioteca.usuarios:
                if u.nome == nome:
                    usuario = u

            for l in biblioteca.livros:
                if l.titulo == titulo:
                    livro = l

            if usuario and livro:
                usuario.pegar_emprestado(livro)
            else:
                print("Usuário ou livro não encontrado.")

        case "4":
            nome = input("Nome do usuário: ")
            titulo = input("Título do livro: ")

            for u in biblioteca.usuarios:
                if u.nome == nome:
                    for l in u.livros_emprestados:
                        if l.titulo == titulo:
                            u.devolver_livro(l)

        case "5":
            biblioteca.listar_livros_disponiveis()

        case "6":
            biblioteca.listar_livros_emprestados()

        case "7":
            print("Encerrando sistema...")
            break

        case _:
            print("Opção inválida.")