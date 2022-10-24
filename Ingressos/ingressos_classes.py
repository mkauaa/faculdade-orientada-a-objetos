class Ingresso():
    codigo = 0
    def __init__(self, valor):
        self._codigo = __class__.codigo + 1
        __class__.codigo += 1
        self._valor = valor
        self._status = False

    @property
    def valor(self):
        return self._valor

    @property
    def status(self):
        return self._status

    # ta imprimindo object at 0x0blablabla
    def __str__(self):
        return f'Código: {self.codigo} \n Valor: {self.valor} \n Status: {self.status}'

class Camarote(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self._adicional = adicional
        self._total = self.valor + self.adicional

    @property
    def adicional(self):
        return self._adicional

    @property
    def total(self):
        return self._total

    def __str__(self):
        return f'Código: {self.codigo} \n Valor: {self.total} \n Status: {self.status}'

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
    def pistas(self, ingresso: Ingresso):
        self._pistas.append(ingresso)

    @property
    def camarotes(self):
        return self._camarotes
    @camarotes.setter
    def pistas(self, ingresso: Ingresso):
        self._camarotes.append(ingresso)

    def __str__(self):
        return f'Artista: {self.artista} \n Data: {self.data} \n Local: {self.local}'

    # a partir daqui tava nas maos de deus

    def gerarIngressos(self, quantidade, valor, tipo = 0):
        self.quantidade = quantidade
        self.valor = valor
        self.tipo = tipo

        if self.tipo == 0:
            for i in range(self.quantidade):
                i = Ingresso(self.valor)
                self.pistas.append(i)

        elif self.tipo == 1:
            self.adicional = int(input('Informe o valor adicional: R$'))
            for i in range(self.quantidade):
                i = Ingresso(self.valor, self.adicional)
                self.camarotes.append(i)
