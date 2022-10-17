from random import randint

class Artista():
    def __init__(self, nome, nacionalidade):
        self.codigo = randint(1000, 1100, 10)
        self.nome = nome
        self.nacionalidade = nacionalidade

    def imprime(self):
        print(f'Nome: {self.nome} \nNacionalidade: {self.nacionalidade}')


class Obra():
    def __init__(self, titulo, tecnica, inovacao, autor:Artista):
        self.codigo = randint(1000, 1100, 10)
        self.titulo = titulo
        self.tecnica = tecnica
        self.inovacao = inovacao
        self.autor = autor

    def avaliar(self):
        # Técnica: 1 - Boa/ 2 - Interessante/ 5 - Excelente
        # Inovação: 2 - Comum/ 4 - Inovadora/ 6 - Única

        global valor
        valor = (self.tecnica * 50 + self.inovacao * 80) * 10
        print(valor)

    def imprimir(self):
        print(f'Código: {self.codigo} \nTítulo: {self.titulo} \nAutor: {self.autor} \nTécnica: {self.tecnica}')
    
    def imprimirObra(self):
        print(f'Código: {self.codigo} \nTítulo: {self.titulo} \nValor: {valor}')


class Pintura(Obra):
    def __init__(self, titulo, tecnica, inovacao, autor: Artista, tinta):
        super().__init__(titulo, tecnica, inovacao, autor)
        self.tinta = tinta

    def imprimir(self):
        print(f'Código: {self.codigo} \nTítulo: {self.titulo} \nAutor: {self.autor} \nTécnica: {self.tecnica} \nTipo de Tinta: {self.tinta}')


class Escultura(Obra):
    def __init__(self, titulo, tecnica, inovacao, autor: Artista, material):
        super().__init__(titulo, tecnica, inovacao, autor)
        self.material = material

    def imprimir(self):
        print(f'Código: {self.codigo} \nTítulo: {self.titulo} \nAutor: {self.autor} \nTécnica: {self.tecnica} \nTipo de Tinta: {self.material}')

class Galeria():
    def __init__(self, nome, telefone, nomeResponsavel):
        self.nome = nome
        self.telefone = telefone
        self.nomeResponsavel = nomeResponsavel

#    def cadastrarObra():

    
#    def cadastrarPintura(self, autor:Artista):


#    def cadastrarEscultura(self, autor:Artista):


#    def pesquisarObras(self, nome):


#    def pesquisarObra(self, codigo):


#    def imprimirObras():