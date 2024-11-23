from .Carta import Carta
from enums.elemento import Elemento
from enums.tipo_monstruo import TipoMonstruo

class CartaMonstruo(Carta):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo, elemento):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo_monstruo = tipo_monstruo
        self.elemento = elemento


    def jugarCarta(self, posicion, modo):
        """Cambia la posición de la carta entre ataque y defensa."""
        self.en_ataque = not self.en_ataque

    def cambioPosicion(self):
        """Verifica si la carta puede ser jugada directamente (sin sacrificios) basado en el número de estrellas."""
        pass

    def fusionar_carta(self, CartaMonstruo):
        pass
    
    def eliminar_carta(self, condicion):
        return super().eliminar_carta(condicion)