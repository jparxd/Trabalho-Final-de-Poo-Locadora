from Src.Operacao.Operacao import Operacao


class Locacao(Operacao):
    def __init__(self, cpf: str, codigo: int, periodo: int):
        super().__init__(cpf, codigo)
        self._periodo = periodo

    def setPeriodo(self, periodo: int):
        self._periodo = periodo

    def getPeriodo(self):
        return self._periodo
