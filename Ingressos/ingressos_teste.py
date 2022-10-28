from ingressos_classes import Ingresso, Camarote, Show

show1=Show('Aviões do forró', '23/06/2022','Arena Aracaju')
show1.gerarIngressos(2,65, 0) #ingresso pista
show1.gerarIngressos(1,32, 1)
#show1.gerarIngressos(5,80,1) #ingresso camarote/VIP
print(show1)
show1.imprimir()
show1.venderIngressos(1, 0)
#print('Valor a pagar por 2 ingressos pista: R$ ',show1.#venderIngresso(2)) # dois ingressos pista
#print('Valor a pagar por 1 ingressos VIP: R$ ',show1.#venderIngresso(1,1)) # um ingresso VIP
#show1.relatorioVendas()
#print('Valor a pagar por 2 ingressos VIP: R$ ',show1.#venderIngresso(2,1)) # dois ingressos VIP
#show1.relatorioVendas()