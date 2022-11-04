class Ingresso():
    cod = 0
    def __init__(self, valor):
        self._codigo = __class__.gerarCodigo()
        self._valor = float(valor)
        self._status = None

    @property
    def codigo(self):
        return self._codigo

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status

    def __str__(self):
        return f'Código: {self.codigo} \nValor: {self.valor} \nStatus: {self.status}'

    @staticmethod
    def gerarCodigo():
        ano = str(date.today())
        Ingresso.cod = Ingresso.cod + 1
        return ano + str(Ingresso.cod)

class Camarote(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self._adicional = float(adicional)

    @property
    def adicional(self):
        return self._adicional
    @adicional.setter
    def adicional(self, adicional):
        self._adicional = adicional

    def __str__(self):
        return f'Código: {self.codigo} \nValor: {self.valor + self.adicional} \nStatus: {self.status}'

class Show():
    def __init__(self, artista, data, local):
        self._artista = artista
        self._data = data
        self._local = local
        self._pistas = []
        self._camarotes = []

    @property
    def artista(self):
        return self._artista

    @property
    def data(self):
        return self._data

    @property
    def local(self):
        return self._local

    @property
    def pistas(self):
        return self._pistas
    @pistas.setter
    def pistas(self, ingresso):
        self._pistas.append(ingresso)

    @property
    def camarotes(self):
        return self._camarotes
    @camarotes.setter
    def camarotes(self, ingresso):
        self._camarotes.append(ingresso)

    def __str__(self):
        return f'\n== SHOW => \nArtista: {self.artista} \nData: {self.data} \nLocal: {self.local}\n'

    def gerarIngressos(self, quantidade, valor, tipo = 0):
        if tipo == 0:
            for i in range(quantidade):
                ingresso = Ingresso(valor)
                self.pistas = ingresso

        elif tipo == 1:
            adicional = int(input('Informe o valor adicional: R$'))
            for i in range(quantidade):
                ingresso = Camarote(valor, adicional)
                self.camarotes = ingresso

    def venderIngresso(self, quantidade, tipo = 0):
        soma = 0
        cont = 0

        if tipo == 0:
            for i in self.pistas:
                if i.status == None and cont != quantidade:
                    i.status = 'Vendido'
                    soma += i.valor
                    cont += 1

        if tipo ==1:
            for i in self.camarotes:
                if i.status == None and cont != quantidade:
                    i.status = 'Vendido'
                    soma += (i.valor + i.adicional)
                    cont += 1

        return soma

    def relatorioVendas(self):
        print(self)
        total = 0
        
        print('= Pista =\n')

        for i in self.pistas:
            if i.status == 'Vendido':
                print(i, '\n')
                total += i.valor

        print('= Camarote =\n')

        for i in self.camarotes:
            if i.status == 'Vendido':
                print(i, '\n')
                total += i.valor + i.adicional

        print(f'Total de vendas = R${total:.2f}\n')
            
        
