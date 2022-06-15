from Src.Operacao.Operacao import Operacao


class Reserva(Operacao):
    def __init__(self, cpf: str, codigo: int):
        super().__init__(cpf, codigo)
        self._prioridade = int()

    def setPrioridade(self, priori: int):
        self._prioridade = priori

    def getPrioridade(self):
        return self._prioridade
