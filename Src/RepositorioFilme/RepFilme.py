from Src.Filme.Filme import Filme


class RepositorioFilme:

    def __init__(self):
        self._filmes = []

    def __repr__(self):
        for filme in self._filmes:
            return f'FILMES: {filme}'

    def cadastrar(self, filme: Filme):
        if self.buscar(filme.getCodigo()) is None:
            self._filmes.append(filme)
        else:
            print("Filme ja existente")

    def buscar(self, codigo: int):
        for filme in self._filmes:
            if codigo == filme.getCodigo():
                return filme
            else:
                return None

    def atualizar(self, filme: Filme):
        filme = self.buscar(filme.getCodigo())
        if filme is not None:
            filme.setPrecoLocacao(filme.getPrecoLocacao())
            filme.setNumeroCopias(filme.getNumeroCopias())
        else:
            print('Erro, nao foi possivel encontrar o filme!!!')

    def deletar(self, codigo: int):
        encontrou = False
        for filme in self._filmes:
            if filme.getCodigo() == codigo:
                self._filmes.pop(self._filmes.index(filme))
                print(f'Filme {filme.getTitulo()} removido com suceesso :D')
                encontrou = True
        if not encontrou:
            print('Filme nao encontrado!!!')

    def listar(self):
        for filme in self._filmes:
            return filme
