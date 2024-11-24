from .carta import Carta

class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, CartaMonstruo, incremento_ataque=0, incremento_defensa=0):
        super().__init__(nombre, descripcion)
        self.incremento_atk = incremento_ataque
        self.incremento_def = incremento_defensa
        self.monstruo_equipado = CartaMonstruo

    def aumentarAtaque(self, CartaMonstruo):
        pass
    
    def aumentarDefensa(self, CartaMonstruo):
        pass

    def eliminarCarta(self):
        pass
    
