from datetime import date


class Filme:

    def __init__(self, codigo: int, titulo: str):
        self._codigo = codigo
        self._titulo = titulo
        self._generos = list()
        self._datalancamento = date.today()
        self._diretor = str()
        self._atores = list()
        self._sinopse = str()
        self._produtores = list()
        self._precoLocacao = float()
        self._numeroCopias = int()

    def __repr__(self):
        return self.imprimir()

    def setCodigo(self, codigo: int):
        self._codigo = codigo

    def getCodigo(self):
        return self._codigo

    def setTitulo(self, titulo: str):
        self._titulo = titulo

    def getTitulo(self):
        return self._titulo

    def setGenero(self, genero: list):
        self._generos = genero

    def getGenero(self):
        return self._generos

    def addGenero(self, genero: str):
        return self._generos.append(genero)

    def setDatadelancamento(self, datalancamento: date):
        self._datalancamento = datalancamento

    def getDatalancamento(self):
        return self._datalancamento

    def setDiretor(self, diretor: str):
        self._diretor = diretor

    def getDiretor(self):
        return self._diretor

    def setAtores(self, atores: list):
        self._atores = atores

    def getAtores(self):
        return self._atores

    def addAtor(self, ator: str):
        return self._atores.append(ator)

    def setSinopse(self, sinopse: str):
        self._sinopse = sinopse

    def getSinopse(self):
        return self._sinopse

    def setProdutores(self, produtores: list):
        self._produtores = produtores

    def getProdutores(self):
        return self._produtores

    def addProdutor(self, produtor: str):
        return self._produtores.append(produtor)

    def setPrecoLocacao(self, precolocacao: float):
        self._precoLocacao = precolocacao

    def getPrecoLocacao(self):
        return self._precoLocacao

    def setNumeroCopias(self, numerocopias: int):
        self._numeroCopias = numerocopias

    def getNumeroCopias(self):
        return self._numeroCopias

    def imprimir(self):
        return f'Codigo: {self._codigo}\nTitulo: {self._titulo}\nGenero: {self._generos}\nData de Lancamento: {self._datalancamento}\nAtores: {self._atores}\nDiretor: {self._diretor}\nSinopse: {self._sinopse}'
