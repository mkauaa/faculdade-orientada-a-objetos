from abc import ABC, abstractmethod
from datetime import datetime, date

class Conta(ABC):
    def __init__(self, data, valor) -> None:
        self.data = datetime.strptime(data, '%d/%m/%Y').date()
        self.valor = valor

class Titulo(Conta):
    def __init__(self, data, valor, fornecedor) -> None:
        super().__init__(data, valor)
        self.fornecedor = fornecedor
        self.status = False

    def getValor(self):
        hoje = date.today()
        if self.data > hoje:
            return self.valor
        else:
            return self.valor * 1.1

    def __str__(self) -> str:
        return f'Titulo: {self.fornecedor} / Data: {self.data} / Valor: R${self.valor}'

class Concessionaria(Conta):
    def __init__(self, data, valor, descricao) -> None:
        super().__init__(data, valor)
        self.descricao = descricao

    def getValor(self):
        return self.valor
    
    def __str__(self) -> str:
        return f'Conta: {self.descricao} / Data: {self.data} / Valor: R${self.valor}'

class Empregado(ABC):
    def __init__(self, nome, sobrenome, id) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.id = id

    def __str__(self) -> str:
        return 'ID: {self.id} / Nome: {self.nome} / Valor: R${self.valor}'

class Assalariado(Empregado):
    def __init__(self, nome, sobrenome, id, hrExtra=None) -> None:
        super().__init__(nome, sobrenome, id)

        if hrExtra == None:
            self.hrExtra = 0
        else:
            self.hrExtra = hrExtra

    def getValor(self):
        salario = float(1100)
        hora = float(8)
        return salario + (self.hrExtra * hora)
        
class Terceirizados(Empregado):
    def __init__(self, nome, sobrenome, id, horas) -> None:
        super().__init__(nome, sobrenome, id)
        self.horas = horas

    def getValor(self):
        hora = float(8)
        return self.horas * hora

class Comissionado(Empregado):
    def __init__(self, nome, sobrenome, id, vendas) -> None:
        super().__init__(nome, sobrenome, id)
        self.vendas = vendas

    def getValor(self):
        hora = float(8)
        return self.vendas * 0.06

class AssalariadoComissionado(Comissionado):
    def __init__(self, nome, sobrenome, id, vendas, comissao=None) -> None:
        super().__init__(nome, sobrenome, id, vendas)
        if comissao == None:
            self.comissao = 0.06
        else:
            self.comissao = int(comissao)/100

    def getValor(self):
        salario = float(1100)
        return salario + self.vendas * self.comissao