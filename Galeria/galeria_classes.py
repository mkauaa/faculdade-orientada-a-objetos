class Galeria():
    def __init__(self, nome, telefone, nomeResponsavel):
        self.nome = nome
        self.telefone = telefone
        self.nomeResponsavel = nomeResponsavel

#    def cadastrarObra():


class Artista():
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def imprime(self):
        print(f'Nome: {self.nome} \nNacionalidade: {self.nacionalidade}')


