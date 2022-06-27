from datetime import date


class Operacao:
    def __init__(self, cpf: str, codigo: int):
        self._cpf = cpf
        self._codigo = codigo
        self._data = date.today()
        self._ativo = bool()

    def setData(self, data: date):
        self._data = data

    def getData(self):
        return self._data

    def setCpf(self, cpf: str):
        self._cpf = cpf

    def getCpf(self):
        return self._cpf

    def setCodigo(self, codigo: int):
        self._codigo = codigo

    def getCodigo(self):
        return self._codigo

    def setAtivo(self, ativo: bool):
        self._ativo = ativo

    def isAtivo(self):
        return self._ativo
