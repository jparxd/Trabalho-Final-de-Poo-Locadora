from Src.Cliente import Cliente


class RepositorioCliente:

    def __init__(self):
        self._clientes = []

    def cadastrar(self, cliente: Cliente):
        if self.buscar(cliente.getCpf()) is None:
            self._clientes.append(cliente)
        else:
            print("Cliente ja existente")

    def buscar(self, cpf: str):
        for cliente in self._clientes:
            return cliente if cpf == cliente.getCpf() else None

    def atualizar(self, cliente: Cliente):
        cliente = self.buscar(cliente.getCpf())
        if cliente is not None:
            cliente.setNome(cliente.getNome())
            cliente.setEndereco(cliente.getEndereco())
        else:
            print('Erro, nao foi possivel encontrar o cliente!!!')

    def deletar(self):
        pass

    def listar(self):
        return self._clientes
