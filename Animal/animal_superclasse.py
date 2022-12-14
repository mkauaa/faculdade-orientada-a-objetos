class Animal:
    def __init__(self, nome, comprimento, patas, cor, ambiente, velocidade):
        self.nome = nome
        self.comprimento = comprimento
        self.patas = patas
        self.cor = cor
        self.ambiente = ambiente
        self.velocidade = velocidade

    def dados(self):
        print(f'Nome: {self.nome}\nComprimento: {self.comprimento} cm\nNum de Patas: {self.patas}')
        print(f'Cor: {self.cor}\nAmbiente: {self.ambiente}\nVelocidade: {self.velocidade} km/h')

class Mamifero(Animal):
    def __init__(self, nome, comprimento, patas, cor, ambiente, velocidade, alimento):
        super().__init__(nome, comprimento, patas, cor, ambiente, velocidade)
        self.alimento = alimento

    def dadosMamifero(self):
        super().dados()
        print(f'Alimento: {self.alimento}')
