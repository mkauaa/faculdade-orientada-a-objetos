from classe_ponto import Circunferencia, Ponto

keke = Ponto(2, 3, 'Verde')

keke.alterar_cor('Azul')

dako = Circunferencia(keke, 5, 'Vermelho', 'Roxo')

dako.perimetro()

dako.imprimir()

print(f'A área equivale a {dako.area()} e o perímetro equivale a {dako.perimetro()}.')

print()
