from datetime import datetime
from datetime import timedelta

from Src.Cliente.Cliente import Cliente
from Src.Filme.Filme import Filme
from Src.Operacao.Operacao import Operacao
from Src.Operacao.Reserva import Reserva
from Src.RepositorioCliente.RepCliente import RepositorioCliente

cliente = Cliente('1234567')
cliente1 = Cliente('3456789')
cliente1.setNome('Jordan')
cliente1.setEndereco('Bell air, 15')
cliente.setNome('Wendel')
cliente.setEndereco('Rua das Flores, 145')


filme = Filme(15, 'O amor')
data = '{:%d/%m/%Y}'.format(datetime(year=2009, month=10, day=20))
filme.setDatadelancamento(data)
filme.setGenero(['Suspense', 'Netorare', 'Jogo do Bixo'])
filme.addGenero('Romance')
filme.setDiretor('Keanu Reeves')
filme.addAtor('Johnny Depp')
filme.setSinopse('Um filme que encanta todos que assistem , sem classificacao indicativa')

despensa = RepositorioCliente()
despensa.cadastrar(cliente)
despensa.cadastrar(cliente)
despensa.cadastrar(cliente1)

cliente.setEndereco('A turma do bairro, 142')
despensa.atualizar(cliente)
for cliente in despensa.listar():
    print(cliente.imprimir())
