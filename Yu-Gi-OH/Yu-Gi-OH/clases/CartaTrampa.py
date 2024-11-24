from .Carta import Carta
from .CartaMonstruo import CartaMonstruo

class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, tipo_atributo):
        super().__init__(nombre, descripcion)
        self.tipo = tipo_atributo

    def impedirAtaque(self, Carta):
        if isinstance(Carta,CartaMonstruo):
            if Carta.elemento == self.tipo:
                1-1
                #Impedir ataque

