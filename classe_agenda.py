class Telefone():
    def init(self, ddd:str, numero:str, descricao:str = '') -> None:
        self.ddd = ddd
        self.numero = numero
        self.descricao = descricao
    
    def alterar_numero(self, numero:str) -> None:
        self.numero = numero
    
    def str(self) -> str:
        return "(" + self.ddd + ") " + self.numero
    
class Contato():
    def init(self, nome:str, e_mail:str, telefone:Telefone) -> None:
        self.nome = nome
        self.email = e_mail
        self.telefone = [telefone]
    
    def alterar_email(self, e_mail:str) -> None:
        self.email = e_mail
    
    def add_telefone(self, telefone:Telefone) -> None:
        if len(self.telefone) <= 3:
            self.telefone.append(telefone)
        else:
            print("Número máximo de telefones cadastrados!")

    def altera_nome(self, nome:str) -> None:
        self.nome = nome
    
    def imprimir(self) -> None:
        wasd = "Contato: {}\nEmail: {}\nTelefone: ".format(self.nome, self.email)
        for tel in self.telefone:
            wasd += str(tel) + " "
        print(wasd)
    
    # A função abaixo tbm permite imprimir na tela fazendo print(contato)
    def str(self) -> str:
        wasd = "Contato: {}\nEmail: {}\nTelefone: ".format(self.nome, self.email)
        for tel in self.telefone:
            wasd += str(tel) + " "
        return wasd

class Agenda():
    def init(self, contatos:Contato) -> None:
        self.contatos = [contatos]
    
    def pesquisar_nome(self, nome:str) -> Contato:
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
    
    def alterar_contato(self, nome_antigo:str, nome_novo:str, e_mail:str, telefone:Telefone) -> None:
        contato_antigo = self.pesquisar_nome(nome_antigo)
        contato_novo = Contato(nome_novo, e_mail, telefone)
        self.contatos[self.contatos.index(contato_antigo)] = contato_novo
    
    def adicionar_contato(self, contato:Contato) -> None:
        if len(self.contatos) <= 100:
            self.contatos.append(contato)
        else:
            print("Agenda cheia!")

tel1 = Telefone("71", "12345")
tel2 = Telefone("45", "78129")
qwerty = Contato("qwerty", "qwerty@gmail.com", tel1)
qwerty.add_telefone(tel2)
minha_agenda = Agenda(qwerty)

print(minha_agenda.pesquisar_nome("qwerty"))