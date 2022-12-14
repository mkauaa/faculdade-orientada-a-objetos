class Ponto:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor

    def alterar_cor(self, novacor = ''):
        self.cor = novacor

    def imprimir(self):
        print(f'Ponto {self.cor} ({self.x}, {self.y})')

class Circunferencia:
    def __init__(self, ponto, raio, cor_linha, cor_preenchimento):
        self.centro = ponto
        self.raio = raio
        self.cor_linha = cor_linha
        self.cor_preenchimento = cor_preenchimento

    def area(self):
        return 3 * (self.raio * self.raio)

    def perimetro(self):
        return 2 * 3 * self.raio

    def imprimir(self):
        print(f'\n==Circunferencia==\n')
        print(f'Centro:', end=' ')
        self.centro.imprimir()
        print(f'\nRaio: {self.raio}\n')
        print(f'Cor da linha: {self.cor_linha}')
        print(f'\nCor do preenchimento: {self.cor_preenchimento}\n')
