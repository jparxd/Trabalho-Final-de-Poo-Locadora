from datetime import datetime
from datetime import timedelta

from Src.Cliente.Cliente import Cliente
from Src.Filme.Filme import Filme
from Src.Operacao.Operacao import Operacao
from Src.Operacao.Reserva import Reserva

cliente = Cliente(1234567)

cliente.setNome('Wendel')
cliente.setEndereco('Rua das Flores, 145')
print(cliente.imprimir())

filme = Filme(15, 'O amor')
data = '{:%d/%m/%Y}'.format(datetime(year=2009, month=10, day=20))
filme.setDatadelancamento(data)
filme.setGenero(['Suspense', 'Netorare', 'Jogo do Bixo'])
filme.addGenero('Romance')
filme.setDiretor('Keanu Reeves')
filme.addAtor('Johnny Depp')
filme.setSinopse('Um filme que encanta todos que assistem , sem classificacao indicativa')

op = Operacao('102030', 2)
pri = Reserva('102030',2)
pri.setPrioridade(1)
print(pri.getPrioridade())

print(filme.imprimir())
