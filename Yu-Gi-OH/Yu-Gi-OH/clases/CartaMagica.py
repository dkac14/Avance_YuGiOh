from .Carta import Carta

class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, incremento_ataque, incremento_defensa,tipo_monstruo):
        super().__init__(nombre, descripcion)
        self.incremento_atk = incremento_ataque
        self.incremento_def = incremento_defensa
        self.elemento = tipo_monstruo


    def aumentarAtaque(self, CartaMonstruo):
        pass
    
    def aumentarDefensa(self, CartaMonstruo):
        pass

    def eliminarCarta(self):
        pass
