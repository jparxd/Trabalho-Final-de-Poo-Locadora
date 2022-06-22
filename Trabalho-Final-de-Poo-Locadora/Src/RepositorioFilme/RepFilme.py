from Src.Filme import Filme


class RepositorioFilme:

    def __init__(self):
        self._filmes = []

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
            filme.setTitulo(filme.getTitulo())
            filme.setGenero(filme.getGenero())
            filme.setDatalancamento(filme.getDatalancamento())
            filme.setDiretor(filme.getDiretor())
            filme.setAtores(filme.getAtores())
            filme.setSinopse(filme.getSinopse())
            filme.setProdutores(filme.getProfutores())
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
        return self._filmes
