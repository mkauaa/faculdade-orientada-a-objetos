from classe_agenda import Agenda, Contato, Telefone

tel1 = Telefone(79, 123, 'Movel')
tel2 = Telefone(79, 456, 'Casa')

mary = Contato('Mary', 'email@email.com', tel1)

mary.alterar_email('marshel@email.com')

mary.add_telefone(tel2)

mary.altera_nome('Shelley')

minha_agenda = Agenda(mary)

print(minha_agenda.pesquisar_nome('Shelley'))

#minha_agenda.alterar_contato('Shelley', 'Maria', 'email@email.com', tel1)

mary.imprimir()


