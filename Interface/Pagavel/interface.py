from abc import ABC, abstractmethod

class Pagavel(ABC):
    @abstractmethod
    def getValor(self):
        pass