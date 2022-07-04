from datetime import datetime
# from datetime import timedelta

from Src.Cliente.Cliente import Cliente
from Src.Filme.Filme import Filme
from Src.Operacao.Operacao import Operacao

# from Src.Operacao.Reserva import Reserva
# from Src.RepositorioCliente.RepCliente import RepositorioCliente
from Src.RepositorioOperacao.RepOpera import RepositorioOperacao

cliente = Cliente('1234567')
cliente.setNome('Wendel')
cliente.setEndereco('Rua das Flores, 145')

cliente1 = Cliente('3456789')
cliente1.setNome('Jordan')
cliente1.setEndereco('Bell air, 15')
uso = Operacao('1020304050', 10)
print(uso.getData())
data1 = '{:%d/%m/%Y}'.format(datetime(year=2004, month=4, day=14))
uso.setData(data1)
print(uso.getData())

filme = Filme(15, 'O amor')
data = '{:%d/%m/%Y}'.format(datetime(year=2009, month=10, day=20))
filme.setDatadelancamento(data)
filme.setGenero(['Suspense', 'Netorare', 'Jogo do Bixo'])
filme.addGenero('Romance')
filme.setDiretor('Keanu Reeves')
filme.addAtor('Johnny Depp')
filme.setSinopse('Um filme que encanta todos que assistem , sem classificacao indicativa')

op = Operacao('124578963', 1)
op1 = Operacao('11122244478',10)
hist = RepositorioOperacao()
hist.cadastrar(op)
hist.cadastrar(op1)
print(hist)
hist.buscarReservas('124578963')