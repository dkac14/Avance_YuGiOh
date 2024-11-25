from .Carta import Carta
from .CartaMonstruo import CartaMonstruo

class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, tipo):
        super().__init__(nombre, descripcion)
        self.tipo = tipo
        self.boca_arriba = False 

    def puede_bloquear(self, monstruo_atacante):
        if (isinstance(monstruo_atacante, CartaMonstruo)):
            return monstruo_atacante.elemento == self.tipo

    def activar(self):
        print(f"{self.nombre} se activa y bloquea el ataque.")

    