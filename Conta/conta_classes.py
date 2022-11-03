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

    def sacar(self, valor):
        if valor > self.saldo:
            return f'Saldo insuficiente.'
        else:
            self.saldo -= valor
            return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def __str__(self):
        return f'Cliente: {self.nomeCliente} \nNº da Conta: {self.numConta} \nSaldo: {self.saldo}'

class ContaPoupanca(Conta):
    def __init__(self, nomeCliente, numConta, saldo, diaRendimento):
        super().__init__(nomeCliente, numConta, saldo)
        
        self._diaRendimento = int(diaRendimento)

    @property
    def diaRendimento(self):
        return self._diaRendimento

    # rendimento mensal?
    def calcularNovoSaldo(self, taxaRendimento):
        self.saldo = self.saldo * taxaRendimento
        return self.saldo

    def __str__(self):
        return f'Cliente: {self.nomeCliente} \nNº da Conta: {self.numConta} \nSaldo: {self.saldo} \nDia do Rendimento: {self.diaRendimento}'

class ContaEspecial(Conta):
    def __init__(self, nomeCliente, numConta, saldo, limite):
        super().__init__(nomeCliente, numConta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self.limite

    def sacarEspecial(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo

        elif self.saldo - valor > self.limite:
            self.saldo -= valor
            return self.saldo

    def __str__(self):
        return f'Cliente: {self.nomeCliente} \nNº da Conta: {self.numConta} \nSaldo: {self.saldo} \nLimite: {self.limite}'
