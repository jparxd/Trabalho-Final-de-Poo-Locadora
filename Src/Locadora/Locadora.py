from Src.Cliente.Cliente import Cliente
from Src.Filme.Filme import Filme
from Src.RepositorioCliente.RepCliente import RepositorioCliente
from Src.RepositorioFilme.RepFilme import RepositorioFilme
from Src.RepositorioOperacao.RepOpera import RepositorioOperacao


class Locadora:

    def __init__(self, clientes: RepositorioCliente, filmes: RepositorioFilme, operacoes: RepositorioOperacao):
        self._clientes = clientes
        self._filmes = filmes
        self._operacoes = operacoes

    def cadastrarCliente(self, cliente: Cliente):
        pass

    def buscarCliente(self, cpf: str):
        pass

    def atualizarCadastroCliente(self, cliente: Cliente):
        pass

    def removerCliente(self, cpf: str):
        pass

    def cadastrarFilme(self, filme: Filme):
        pass

    def buscarFilme(self, codigo: int):
        pass

    def atualizarCadastroFilme(self, filme: Filme):
        pass

    def removerFilme(self, codigo: int):
        pass

    def reservarFilme(self, cpf: str, codigo: int):
        pass

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
