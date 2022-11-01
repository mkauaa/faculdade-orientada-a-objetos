from ingressos_classes import Show

show1=Show('Aviões do forró', '23/06/2022','Arena Aracaju')

show1.gerarIngressos(5,80)

show1.gerarIngressos(5,80,1)

print(f'Valor a pagar por 2 ingressos pista: R${show1.venderIngresso(2)}')

print(f'Valor a pagar por 1 ingressos VIP: R${show1.venderIngresso(1,1)}')

show1.relatorioVendas()

print(f'Valor a pagar por 2 ingressos VIP: R${show1.venderIngresso(2,1)}')

show1.relatorioVendas()