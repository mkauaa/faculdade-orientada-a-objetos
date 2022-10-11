class Vaca:
    def __init__(self):
        self.registro = ''
        self.raca = ''
        self.cor = ''
        self.tamanho = 0.0
        self.idade = 0
        self.peso = 0.0
        self.leite = 0.0


    def comer(self, alimento, quant):
        self.peso += quant * 0.05
        print(f'Vaca comendo {quant} kg de {alimento}.')


    def produzirLeite(self):
        self.leite = self.peso * 0.02
        return self.leite


    def caminhar(self, distancia):
        print(f'Vaca caminhando {distancia} km.')
