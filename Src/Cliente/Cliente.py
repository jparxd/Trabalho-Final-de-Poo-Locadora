class Cliente:

    def __init__(self, cpf: int):
        self._cpf = cpf
        self._nome = str()
        self._endereco = str()

    def setCpf(self, cpf: int):
        self._cpf = cpf

    def getCpf(self):
        return self._cpf

    def setNome(self, nome: str):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setEndereco(self, endereco: str):
        self._endereco = endereco

    def getEndereco(self):
        return self._endereco

    def imprimir(self):
        return f'Nome: {self._nome}\nEndereco: {self._endereco}'
