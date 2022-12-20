class Poliedro:
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

class Cilindro:
    def __init__(self, raio, altura):
        self.raio = raio
        self.altura = altura

    def calculaArea(self):
        return {2 * 3.14 * self.raio(self.altura + self.raio)}

    def calculaVolume(self):
        return {3,14 * self.raio * self.raio * self.altura}

    def __str__(self):
        return f'Area: {self.calculaArea}\n Volume: {self.calculaVolume}'

