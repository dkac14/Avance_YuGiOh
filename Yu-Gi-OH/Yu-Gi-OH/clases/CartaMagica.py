from .Carta import Carta
from .CartaMonstruo import CartaMonstruo

class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, incremento_ataque, incremento_defensa,tipo_monstruo):
        super().__init__(nombre, descripcion)
        self.incremento_atk = incremento_ataque
        self.incremento_def = incremento_defensa
        self.elemento = tipo_monstruo

    def sePuedeActivar(self, lista_cartas):
        for elem in lista_cartas:
            if (isinstance(elem, CartaMonstruo)) and elem.tipo_monstruo == self.elemento:
                return True

    def monstruoActivar(self, lista_cartas):
        for elem in lista_cartas:
            if (isinstance(elem, CartaMonstruo)) and elem.tipo_monstruo == self.elemento:
                return elem

    def ActivarEfecto(self, monstruo):
        if (isinstance(monstruo, CartaMonstruo)):
            if self.incremento_atk > 0:
                monstruo.ataque += self.incremento_atk
                print(f"{self.nombre} equipada a {monstruo.nombre}. Incrementa su ataque en {self.incremento_atk}.")
            else: 
                monstruo.defensa += self.incremento_def
                print(f"{self.nombre} equipada a {monstruo.nombre}. Incrementa su defensa en {self.incremento_def}.")


    def aumentarAtaque(self, CartaMonstruo):
        pass
    
    def aumentarDefensa(self, CartaMonstruo):
        pass

    def eliminarCarta(self):
        pass

    def __str__(self):
        return (f"{self.nombre}: {self.descripcion}\n")
                
