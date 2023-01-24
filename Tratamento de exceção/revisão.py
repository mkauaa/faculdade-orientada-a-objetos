from abc import ABC, abstractmethod
from datetime import datetime, date

class iAutenticavel(ABC):
    @abstractmethod
    def autenticar(self):
        pass

class SaldoExcecaoError(Exception):
    pass

def validarSaque(self, saque):
    if saque > self.saldo:
        raise SaldoExcecaoError('Saque maior que o saldo.')

class Conta:
    def __init__(self, agencia=str, numConta=int, saldo=0, senha=str):
        self.agencia = agencia
        self.numConta = numConta
        self.saldo = 0
        self.senha = senha
    
    def autenticar(self, senha1) -> bool:
        if senha1 == self.senha:
            return True
        else:
            return False
    
    def depositar(self, valor) -> float:
        try:
            self.saldo += valor
        except TypeError:
            print('Erro: Tipo Inválido!')
       

    def sacar(self) -> float:
        try:
            s = input(float('Valor a ser sacado: '))
            validarSaque(s)
        except SaldoExcecaoError as e:
            print(f'ERRO {e}')
    
    def __str__(self) -> str:
        return 'Agencia: {0} Conta; {1} Saldo atual: {2} Senha: {3}'.format(self.agencia, self.numConta, self.saldo, self.senha)
    


class ContaPoupanca(Conta):
    def __init__(self, agencia=str, numConta=int, saldo=0, senha=str, percRendimento=float, diaRendimento=date):
        super().__init__(agencia, numConta, saldo, senha)
        self.percRendimento = percRendimento
        self.diaRendimento = diaRendimento
    
    def autenticar(self, senha) -> bool:
        if senha == self.senha:
            return True
        else:
            return False

    def calcularRendimento(self):
        if date.today() == self.diaRendimento:
            s = (self.saldo + self.percRendimento/100)
            self.saldo = s


class ContaEspecial(Conta):
    def __init__(self, agencia=str, numConta=int, saldo=0, senha=str, limite=float, juros=float):
        super().__init__(agencia, numConta, saldo, senha)
        self.limite = limite
        self.juros = juros
    
    def autenticar(self, senha) -> bool:
        if senha == self.senha:
            return True
        else:
            return False

    def debitarJuros(self, data):
        self.data = datetime.strptime(data, '%d/%m/%y').date()

        #hoje = date.today()
        if self.data == ('01/%m/%y'):
           self.saldo = self.saldo - self.juros


a = Conta('uai', 12, 'help')
print(a)
a.depositar(10)
print(a)