from datetime import date

class Conta():
    def __init__(self, nomeCliente, numConta, saldo):
        self._nomeCliente = nomeCliente
        self._numConta = numConta
        self._saldo = saldo

    @property
    def nomeCliente(self):
        return self._nomeCliente

    @property
    def numConta(self):
        return self._numConta

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def __str__(self):
        return f'Cliente: {self.nomeCliente} \nNº da Conta: {self.numConta} \nSaldo: R${self.saldo:.2f}\n'

class ContaPoupanca(Conta):
    def __init__(self, nomeCliente, numConta, saldo, diaRendimento):
        super().__init__(nomeCliente, numConta, saldo)
        self.hoje = date.today().day
        
        self._diaRendimento = int(diaRendimento)

    @property
    def diaRendimento(self):
        return self._diaRendimento

    def calcularNovoSaldo(self, taxaRendimento):
        if self.hoje >= self.diaRendimento:
            self.saldo = self.saldo + self.saldo * taxaRendimento
        return self.saldo

    def __str__(self):
        return f'Cliente: {self.nomeCliente} \nNº da Conta: {self.numConta} \nSaldo: R${self.saldo:.2f} \nDia do Rendimento: {self.diaRendimento}\n'

class ContaEspecial(Conta):
    def __init__(self, nomeCliente, numConta, saldo, limite):
        super().__init__(nomeCliente, numConta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self, limite):
        self._limite = limite
        return self._limite

    def sacarEspecial(self, valor):
        if self.saldo >= 0:
            if valor <= self.saldo + self.limite:
                if self.saldo >= valor:
                    self.sacar(valor)
                else:
                    excede = self.saldo - valor
                    self.limite -= (- excede)
                    self.saldo = excede

            else:
                print(f'Limite insuficiente.')  

        else:
            if self.limite - valor < 0:
                    print(f'Limite insuficiente.')   
            else:
                self.saldo = self.saldo - valor
                self.limite = self.limite - valor

    def __str__(self):
        return f'Cliente: {self.nomeCliente} \nNº da Conta: {self.numConta} \nSaldo: R${self.saldo:.2f} \nLimite: {self.limite}\n'
