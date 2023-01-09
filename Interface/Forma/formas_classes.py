from iformageometrica import iFormaGeometrica
import math


class Cilindro(iFormaGeometrica):
    def __init__(self, raio, altura):
        self.raio = raio
        self.altura = altura

    def calculaArea(self):
        area = 2 * math.pi * self.raio * (self.altura + self.raio)
        return area

    def calculaVolume(self):
        volume = math.pi * self.raio * self.raio * self.altura
        return volume

    def __str__(self):
        return f'Area: {self.calculaArea}\n Volume: {self.calculaVolume}'

class Poliedro(iFormaGeometrica):
    def __init__(self, vertices, arestas, faces, l1, l2, altura):
        self.vertices = vertices
        self.arestas = arestas
        self.faces = faces
        self.l1 = l1
        self.l2 = l2
        self.altura = altura

    def convexo(self):
        if self.vertices - self.arestas + self.faces == 2:
            return True
        else:
            return False

    def __str__(self):
        s = f'Area: {self.calculaArea}\mVolume: {self.calculaVolume}'
        if self.convexo():
            s += 'O poliedro é convexo.'
        else:
            s += 'O poliedro não é convexo.'
            
        return s

class Cubo(Poliedro):
    def __init__(self, lado):
        super().__init__(self)
        self.lado = lado
        self.vertices = 12
        self.arestas = 8
        self.faces = 6

    def calculaArea(self):
        area = 6 * (math.pow(self.lado, 2))
        return area

    def calculaVolume(self):
        volume = math.pow(self.lado, 3)
        return volume

class Retangulo(Poliedro):
    def __init__(self, altura, comprimento, largura):
        super().__init__(self, altura)
        self.altura = altura
        self.comprimento = comprimento
        self.largura = largura
        self.vertices = 12
        self.arestas = 8
        self.faces = 6

    def calculaArea(self):
        area = 2 * (self.largura * self.comprimento + self.comprimento * self.altura + self.largura * self.comprimento)
        return area

    def calculaVolume(self):
        volume = self.altura * self.comprimento * self.largura
        return volume


# PRINCIPAL #

iFormaGeometrica.register(Poliedro)
iFormaGeometrica.register(Cilindro)

cubo = Cubo(5)
print(cubo)

retangulo = Retangulo(2, 3, 4)
print(retangulo)

cilindro = Cilindro(2, 5)
print(cilindro)

