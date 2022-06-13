from Src.Cliente.Cliente import Cliente
from Src.Filme.Filme import Filme

cliente = Cliente(1234567)

cliente.setNome('Wendel')
cliente.setEndereco('Rua das Flores, 145')
print(cliente.imprimir())


filme = Filme(15,'O amor')
