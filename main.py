from datetime import date

from Src.Cliente.Cliente import Cliente
from Src.Filme.Filme import Filme
from Src.Locadora.Locadora import Locadora
from Src.Operacao.Locacao import Locacao
from Src.Operacao.Reserva import Reserva
from Src.RepositorioCliente.RepCliente import RepositorioCliente
from Src.RepositorioFilme.RepFilme import RepositorioFilme
from Src.RepositorioOperacao.RepOpera import RepositorioOperacao

if __name__ == '__main__':

    # cli = Cliente()
    # ope = Operacao()
    # loc = Locacao()
    # reserva = Reserva()
    cliente = RepositorioCliente()
    filme = RepositorioFilme()
    operacao = RepositorioOperacao()
    locadora = Locadora(cliente, filme, operacao)
    # menu principal
    while True:
        op = int(input('[1] - Filmes\n[2] - Clientes\n'))
        if op == 1:
            flag = True
            while flag is True:
                option = int(input(
                    '[1] - Cadastrar filme\n'
                    '[2] - Visualizar filmes\n'
                    '[3] - Reservar filmes\n'
                    '[4] - Alugar filmes\n'
                    '[5] - Modificar filmes\n'
                    '[6] - Top filmes\n'
                    '[7] - Deletar filmes\n'
                    '[8] - Home\n'))
                if option == 1:
                    movie = Filme(int(input('Codigo:\n')), input('Titulo:\n'))
                    movie.setGenero([input('Genero do filme:\n')])
                    movie.setDatadelancamento(date.today())
                    movie.setDiretor(input('Diretor:\n'))
                    movie.setAtores([input('Atores:\n')])
                    movie.setSinopse(input('Sinopse:\n'))
                    movie.setProdutores([input('Produtores:')])
                    movie.setPrecoLocacao(float(input('Preço da locação:\n')))
                    movie.setNumeroCopias(int(input('Numero de copias:\n')))
                    locadora.cadastrarFilme(movie)
                elif option == 2:
                    print(filme.listar())

                elif option == 3:
                    client = input('CPF do cliente:\n')
                    code = int(input('Codigo do filme:\n'))
                    operation = Reserva(client, code)
                    fi = filme.buscar(code)
                    if cliente.buscar(client) is not None:
                        if fi is not None:
                            if operacao.numeroLocacoesAtivas(code) == fi.getNumeroCopias():
                                operacao.cadastrar(operation)
                elif option == 4:
                    client = input('CPF do cliente:\n')
                    code = int(input('Codigo do filme:\n'))
                    period = int(input('Periodo de locação:'))
                    operation = Locacao(client, code, period)
                    fi = filme.buscar(code)
                    if cliente.buscar(client) is not None:
                        if fi is not None:
                            if operacao.numeroLocacoesAtivas(code) == fi.getnumerocopias():
                                operacao.cadastrar(operation)

                elif option == 5:
                    a = filme.buscar(int(input("Digite o codigo do filme que deseja modificar: \n")))
                    if a is not None:
                        a.setPrecoLocacao(float(input("Digite o novo preco do filme: ")))
                        a.setNumeroCopias(int(input("Digite o novo numero de copias: ")))
                        filme.atualizar(a)
                elif option == 6:
                    pass
                elif option == 7:
                    b = filme.buscar(int(input("Digite o codigo do filme que deseja deletar: \n")))
                    if b is not None:
                        filme.deletar(int(input("Para confirmar digite o codigo novamente: \n")))

                elif option == 8:
                    flag = False

        if op == 2:
            flag = True
            while flag is True:
                option = int(input(
                    '\n'
                    '[1] - Cadastrar cliente\n'
                    '[2] - Visualizar cliente\n'
                    '[3] - Atualizar cadastro\n'
                    '[4] - Deletar cadastro\n'
                    '[5] - Devolver filme\n'
                    '[6] - Home\n'))
                if option == 1:
                    user = Cliente(input('CPF: \n'))
                    user.setNome(input('Nome:\n'))
                    user.setEndereco(input('Endereço:\n'))
                    cliente.cadastrar(user)

                elif option == 2:
                    cpf = input('Digte o CPF do cliente que deseja visualisar:\n')
                    user = cliente.buscar(cpf)
                    if user is not None:
                        print(user)
                        locadora.imprimirHistoricoLocacoes(cpf)
                elif option == 3:
                    c = cliente.buscar(input("Digite o cpf do cliente que deseja modificar: \n"))
                    if c is not None:
                        c.setNome(input("Digite o novo nome do cliente: "))
                        c.setEndereco(input("Digite o novo endereco do cliente: "))
                        cliente.atualizar(c)
                elif option == 4:
                    locadora.removerCliente(input('Digite o CPF do client que deseja remover:\n'))
                elif option == 5:
                    cpf = input('Digite o CPF do cliente:\n')
                    cod = int(input('Digute o codigo do filme que deseja devolver:\n'))
                    user = cliente.buscar(cpf)
                    fi = filme.buscar(cod)
                    if user is not None:
                        if fi is not None:
                            operacao.deletarLocacao(cpf, cod)
                elif option == 6:
                    flag = False
