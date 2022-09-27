class Agenda:
    def __init__(self):
        self.contatos = []

    def pesquisar_nome(self, nome):

    def alterar_contato(self, nome):

    def add_contato(self, contato):
        self.contatos.append(contato)

class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def alterar_email(self, email):
        self.email = email

    def add_telefone(self, telefone):
        self.telefone.append(telefone)

    def alterar_nome(self, nome):
        self.nome = nome

    def imprimir(self):
        print(f'Nome: {self.nome}'
        f'E-Mail: {self.email}'
        f'Telefone: {self.telefone}')

class Telefone:
    def __init__(self, ddd, num, descricao):
        self.ddd = ddd
        self.numero = num
        self.descricao = descricao

    def alterar_num(self, num):
        self.numero = num
