from contas import Conta
from interface import Pagavel
from datetime import date

class Controle:
    def __init__(self) -> None:
        self.listaPagaveis = []

    def addPagaveis(self, pagavel):
        if isinstance(pagavel, Pagavel):
            self.listaPagaveis.append(pagavel)

    def relatorioContas(self):
        soma = 0
        print('== Relatório de Contas do Mês %.2d'%date.today().month)

        for elemento in self.listaPagaveis:
            if isinstance(elemento, Conta):
                soma += elemento.getValor()
                print(elemento)

        print(f'Valor total: R${float(soma)}')
        return float(soma)

    def relatorioPessoal(self):
        print('== Relatório Geral do Mês ==')
        valorContas = self.relatorioContas()
        valorPessoal = self.relatorioPessoal()
        print('Valor Total do mês: R$', valorContas + valorPessoal)