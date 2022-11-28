from abc import ABC, abstractmethod

class Pessoa():
    def __init__(self, nome, sobrenome, email) -> None:
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
    def __init__(self, nome, sobrenome, email) -> None:
        super().__init__(nome, sobrenome, email)
        self._cartoes = []

    @property
    def cartoes(self):
        return self._cartoes
    @cartoes.setter
    def cartoes(self, cartao):
        self._cartoes.append(cartao)

    def addCartao(self, cartao):
        self.cartoes = cartao

'''    def showCartao(cartao):
        print(f'Destinatário: {} {} \nMensagem do cartão: {} \n Mensagem adicional: {} \nAss: {} {}')'''


class Cartao(ABC):
    def __init__(self, destinatario: Pessoa, messagePlus = ''):
        self._destinatario = destinatario
        self._messagePlus = messagePlus

    @property
    def destinatario(self):
        return self._destinatario
    @property
    def messagePlus(self):
        return self._messagePlus
    @messagePlus.setter
    def messagePlus(self, message):
        self._messagePlus = message

    @abstractmethod
    def showMessage(self):
        print(self.messagePlus)


class DiaNamorados(Cartao):
    def __init__(self, destinatario: Pessoa, messagePlus=''):
        super().__init__(destinatario, messagePlus)
        self._messagePlus = "\n'When darkness comes\nAnd pain is all around\nLike a bridge over troubled water\nI will lay me down'\n"


class Natal(Cartao):
    def __init__(self, destinatario: Pessoa, messagePlus=''):
        super().__init__(destinatario, messagePlus)
        self._messagePlus = "\n'This year\nTo save me some tears\I'll give it to someone special'\n"


class Aniversario(Cartao):
    def __init__(self, destinatario: Pessoa, messagePlus=''):
        super().__init__(destinatario, messagePlus)
        self._messagePlus = "\n'All those people said\nWe wouldn't last a minute near\nI'm with you\nAnd I could roll into another year'\n"       
