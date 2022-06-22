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
            if cpf == cliente.getCpf():
                return cliente
            else:
                return None

    def atualizar(self, cliente: Cliente):
        cliente = self.buscar(cliente.getCpf())
        if cliente is not None:
            cliente.setNome(cliente.getNome())
            cliente.setEndereco(cliente.getEndereco())
        else:
            print('Erro, nao foi possivel encontrar o cliente!!!')

    def deletar(self, cpf: str):
        encontrou = False
        for cliente in self._clientes:
            if cliente.getCpf() == cpf:
                self._clientes.pop(self._clientes.index(cliente))
                print(f'Cliente {cliente.getNome()} removido com suceesso :D')
                encontrou = True
        if not encontrou:
            print('Cliente nao encontrado!!!')

    def listar(self):
        return self._clientes
