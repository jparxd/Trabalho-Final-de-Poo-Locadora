from Src.Operacao.Operacao import Operacao
from Src.Operacao.Reserva import Reserva


class RepositorioOperacao:

    def __init__(self):
        self.operacoes = []

    def __repr__(self):
        return f'OPERACOES: {self.operacoes}'

    def cadastrar(self, operacao: Operacao):
        if operacao not in self.operacoes:
            self.operacoes.append(operacao)
            operacao.setAtivo(True)
        else:
            print('Operacao ja cadastrada!!')

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
