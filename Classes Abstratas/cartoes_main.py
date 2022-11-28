from cartoes import Pessoa, Remetente, Cartao, Aniversario, DiaNamorados, Natal

remetente=Remetente('Cris','Oliveira','cris@gmail.com')
destinatario=Pessoa('Maria','Oliveira','maria@gmail.com')
cartao= Aniversario(destinatario,'Felicidades')
remetente.addCartoes(cartao)
remetente.showCartao(cartao)
cartao2 = Natal(destinatario)
remetente.addCartoes(cartao2)
remetente.showCartao(cartao2)
cartaoN=Cartao(destinatario)