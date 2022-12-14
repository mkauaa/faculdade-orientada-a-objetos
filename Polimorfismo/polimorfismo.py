class Quadrilatero:
    def __init__(self, base, altura=None):
        self._base = base
        self._altura = altura
        if self.altura == None:
            self.altura = self.base

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def calcula_area(self):
        return self.base * self.altura

    def calcula_perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f'Base: {self.base} / Altura: {self.altura}'


class Losango(Quadrilatero):
    def __init__(self, lado, diagonal_maior, diagonal_menor):
        self._lado = lado
        self._diagonal_maior = diagonal_maior
        self._diagonal_menor = diagonal_menor

    @property
    def lado(self):
        return self._lado

    @property
    def diagonal_maior(self):
        return self._diagonal_maior

    @property
    def diagonal_menor(self):
        return self._diagonal_menor

    def calcula_area(self):
        return self.diagonal_maior * self.diagonal_menor / 2

    def calcula_perimetro(self):
        return self.lado * 4    

    def __str__(self):
        return f'Lado: {self.lado} / D. Maior: {self.diagonal_maior} / D. Menor: {self.diagonal_menor}'  


class Trapezio(Quadrilatero):
    def __init__(self, base_maior, base_menor, altura, lado1, lado2):
        self._base_maior = base_maior
        self._base_menor = base_menor
        self._altura = altura
        self._lado1 = lado1
        self._lado2 = lado2

    @property
    def base_maior(self):
        return self._base_maior

    @property
    def base_menor(self):
        return self._base_menor

    @property
    def altura(self):
        return self._altura

    @property
    def lado1(self):
        return self._lado1

    @property
    def lado2(self):
        return self._lado2

    def calcula_area(self):
        return (self.base_maior + self.base_menor) * self.altura / 2

    def calcula_perimetro(self):
        return self.base_maior + self.base_menor + self.lado1 + self.lado2

    def __str__(self):
        return f'Base Maior: {self.base_maior} / Base Menor: {self.base_menor} / Altura: {self.altura} / Lado 1: {self.lado1} / Lado 2: {self.lado2}'  
       

# Principal

quadrado = Quadrilatero(10)

print(quadrado)
print(f'- ??rea quadrado: {quadrado.calcula_area()}')
print(f'- Per??metro quadrado: {quadrado.calcula_perimetro()}\n')

retangulo = Quadrilatero(4, 5)

print(retangulo)
print(f'- ??rea ret??ngulo: {retangulo.calcula_area()}')
print(f'- Per??metro ret??ngulo: {retangulo.calcula_perimetro()}\n')

losango = Losango(8, 12, 7)

print(losango)
print(f'- ??rea losango: {losango.calcula_area()}')
print(f'- Per??metro losango: {losango.calcula_perimetro()}\n')

trapezio = Trapezio(5, 4, 8, 10, 15)

print(trapezio)
print(f'- ??rea trapezio: {trapezio.calcula_area()}')
print(f'- Per??metro trapezio: {trapezio.calcula_perimetro()}\n')
