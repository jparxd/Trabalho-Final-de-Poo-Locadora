from Src.Cliente.Cliente import Cliente
from Src.Filme.Filme import Filme
from Src.Operacao.Locacao import Locacao
from Src.Operacao.Operacao import Operacao
from Src.Operacao.Reserva import Reserva
from Src.RepositorioCliente.RepCliente import RepositorioCliente
from Src.RepositorioFilme.RepFilme import RepositorioFilme
from Src.RepositorioOperacao.RepOpera import RepositorioOperacao


class Locadora:

    def __init__(self, clientes: RepositorioCliente, filmes: RepositorioFilme, operacoes: RepositorioOperacao):
        self._clientes = clientes
        self._filmes = filmes
        self._operacoes = operacoes

    def cadastrarCliente(self, cliente: Cliente):
        self._clientes.cadastrar(cliente)

    def buscarCliente(self, cpf: str):
        return self._clientes.buscar(cpf)

    def atualizarCadastroCliente(self, cliente: Cliente):
        self._clientes.atualizar(cliente)

    def removerCliente(self, cpf: str):
        if self._operacoes.numeroLocacoesAtivas(cpf) == 0:
            self._clientes.deletar(cpf)

    def cadastrarFilme(self, filme: Filme):
        self._filmes.cadastrar(filme)

    def buscarFilme(self, codigo: int):
        return self._filmes.buscar(codigo)

    def atualizarCadastroFilme(self, filme: Filme):
        self._filmes.atualizar(filme)

    def removerFilme(self, codigo: int):
        if self._operacoes.numeroLocacoesAtivas(codigo) == 0:
            self._filmes.deletar(codigo)

    def reservarFilme(self, cpf: str, codigo: int):
        op = Reserva(cpf, codigo)
        if self.buscarCliente(cpf) is not None:
            if self.buscarFilme(codigo) is not None:
                self._operacoes.cadastrar(op)


    def finalizarReservaFilme(self, cpf: str, codigo: int):
        pass

    def locarFilme(self, cpf: str, codigo: int):
        pass

    def devolverFilme(self, cpf: str, codigo: int):
        pass

    def imprimirHistoricoLocacoes(self, cpf: str):
        pass

    def imprimirFilmesMaisLocados(self, top: int):
        pass
