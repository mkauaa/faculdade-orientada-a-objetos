from contas import Conta, Concessionaria, Titulo, Assalariado, AssalariadoComissionado, Comissionado, Terceirizados, Empregado
from interface import Pagavel
from datetime import date
from controle import Controle

Pagavel.register(Conta)
Pagavel.register(Empregado)

cp = Controle()
c1 = Concessionaria('28/12/2022', 450.10, 'Energisa')
cp.addPagaveis(c1)

cp = Controle()
t1 = Titulo('18/12/2022', 1000, 'Destak')
cp.addPagaveis(t1)

c2 = Concessionaria('15/12/2022', 180.98, 'Deso')
cp.addPagaveis(c2)
t2 = Titulo('20/12/2022', 300, 'TH Mix')

cp.addPagaveis(t2)
t3 = Titulo('22/12/2022', 200, 'Maratá')
cp.addPagaveis(t3)

cp.relatorioContas()
print()

##

e1 = Assalariado('Joao', 'de Barro', '001', 2)
cp.addPagaveis(e1)

e2 = Assalariado('Ana', 'de Jesus', '002', 20)
cp.addPagaveis(e2)

e3 = Assalariado('Andre', 'Casagrande', '003', 700)
cp.addPagaveis(e3)

e4 = AssalariadoComissionado('Catarina', 'Sofia', '004', 400, 10)
cp.addPagaveis(e4)

cp.relatorioPessoal()
print()