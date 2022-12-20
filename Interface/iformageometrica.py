from abc import ABC, abstractmethod

class iFormaGeometrica(ABC):
    @abstractmethod
    def calculaArea(self):
        pass

    @abstractmethod
    def calculaVolume(self):
        pass
