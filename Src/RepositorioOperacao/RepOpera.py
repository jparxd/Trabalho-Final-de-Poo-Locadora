from Src.Operacao.Locacao import Locacao
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
        reserva = []
        for operacao in self.operacoes:
            if operacao.getCpf() == cpf and operacao.isAtivo() is True and isinstance(operacao, Reserva):
                reserva.append(operacao)
        return reserva

    def buscarLocacoes(self, cpf: str):
        locacao = []
        for operacao in self.operacoes:
            if operacao.getCpf() == cpf and operacao.isAtivo() is True and isinstance(operacao, Locacao):
                locacao.append(operacao)
        return locacao

    def deletarReservas(self, cpf: str, codigo: int):
        for operacao in self.operacoes:
            if operacao.getCpf() == cpf and operacao.getCodigo() == codigo and operacao.isAtivo() is True and isinstance(
                    operacao, Reserva):
                operacao.setAtivo(False)

    def deletarLocacao(self, cpf: str, codigo: int):
        for operacao in self.operacoes:
            if operacao.getCpf() == cpf and operacao.getCodigo() == codigo and operacao.isAtivo() is True and isinstance(
                    operacao, Locacao):
                operacao.setAtivo(False)

    def listarLocacoes(self, cpf: str):
        locacoes = []
        for operacao in self.operacoes:
            if operacao.getCpf() == cpf and isinstance(operacao, Locacao):
                locacoes.append(operacao)
        return locacoes

    def numeroLocacoes(self, cpf: str):
        num = self.listarLocacoes(cpf)
        return len(num)

    def numeroLocacoes(self, codigo: int):
        pass

    def numeroLocacoesAtivas(self, cpf: str):
        pass

    def numeroLocacoesAtivas(self, codigo: int):
        pass

    def numeroReservas(self, codigo: int):
        pass
