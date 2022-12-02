class Pessoa:
    def __init__(self, nome, sobrenome, email) -> str:
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def sobrenome(self):
        return self._sobrenome
    
    @property
    def email(self):
        return self._email


class Remetente(Pessoa):
    def __init__(self, nome, sobrenome, email, *cartao) -> str:
        super().__init__(nome, sobrenome, email)
        self._lista = []
        for c in cartao:
            self._lista.append(c)
    
    @property
    def lista(self):
        return self._lista
    @lista.setter
    def lista(self, cartao):
        self._lista.append(cartao)

    def addCartao(self, cartao):
        self.lista = cartao
    
    def showCartao(self, cartao):
        return f'Nome do destinatário: {self.nome}, {self.sobrenome}\nMensagem do cartão: \nMensagem particular: \nAss: '
