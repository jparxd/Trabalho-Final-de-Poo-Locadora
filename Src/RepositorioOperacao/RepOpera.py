from Src.Operacao.Operacao import Operacao


class RepositorioOperacao:

    def __init__(self):
        self.operacao = []

    def cadastrar(self, operacao: Operacao):
        pass

    def buscarReservas(self, cpf: str):
        pass

    def buscarLocacoes(self, cpf: str):
        pass

    def deletarReservas(self, cpf: str, codigo: int):
        pass

    def deletarLocacao(self, cpf: str, codigo: int):
        pass

    def listarLocacoes(self, cpf: str):
        pass

    def numeroLocacoes(self, cpf: str):
        pass

    def numeroLocacoes(self, codigo: int):
        pass

    def numeroLocacoesAtivas(self, cpf: str):
        pass

    def numeroLocacoesAtivas(self, codigo: int):
        pass

    def numeroReservas(self, codigo: int):
        pass
