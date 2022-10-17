class Telefone():
    def __init__(self, ddd, numero, descricao = ''):
        self.ddd = ddd
        self.numero = numero
        self.descricao = descricao
    
    def alterar_numero(self, numero):
        self.numero = numero
    
    def str(self):
        return  f'({self.ddd}) {self.numero}'
    
class Contato():
    def __init__(self, nome, e_mail, telefone:Telefone):
        self.nome = nome
        self.email = e_mail
        self.telefone = [telefone]
    
    def alterar_email(self, e_mail):
        self.email = e_mail
    
    def add_telefone(self, telefone:Telefone):
        if len(self.telefone) <= 3:
            self.telefone.append(telefone)
        else:
            print("Número máximo de telefones cadastrados!")

    def altera_nome(self, nome):
        self.nome = nome
    
    def imprimir(self):
        dados = f'Contato: {self.nome} \nEmail: {self.email} \nTelefone(s): '
        for tel in self.telefone:
            dados += str(tel) + " "
        print(dados)

class Agenda():
    def __init__(self, contatos:Contato):
        self.contatos = [contatos]
    
    def pesquisar_nome(self, nome) -> Contato:
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
    
    def alterar_contato(self, nome_antigo, nome_novo, e_mail, telefone:Telefone):
        contato_antigo = self.pesquisar_nome(nome_antigo)
        contato_novo = Contato(nome_novo, e_mail, telefone)
        self.contatos[self.contatos.index(contato_antigo)] = contato_novo
    
    def adicionar_contato(self, contato:Contato):
        if len(self.contatos) <= 100:
            self.contatos.append(contato)
        else:
            print("Agenda cheia!")
