from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv...")


    def desligar(self):
        print("Desligando a tv...")
        print("Desligado!")

    @property
    def marca(self):
        return "PHILCO"
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar condicionado...")


    def desligar(self):
        print("Desligando o ar condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle2 = ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca)
