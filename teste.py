from arquivo import Vaca

Kate = Vaca()

Kate.peso = 50

print(Kate.peso)
Kate.comer('Grama', 15)
print(Kate.peso)

Kate.produzirLeite()
print(f'Kate produziu {Kate.leite:.1f} L de leite')
