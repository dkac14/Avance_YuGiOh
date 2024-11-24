from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa

class Tablero:
    def __init__(self):
        self.cartas_monstruo = []
        self.cartas_trampa = []
        self.cartas_magica = []

    def agregar_carta_monstruo(self, carta):
        if len(self.cartas_monstruo) < 3 and isinstance(carta, CartaMonstruo):
            self.cartas_monstruo.append(carta)
        else:
            print("No hay espacio para más cartas de monstruo en el tablero.")

    def agregar_carta_trampa(self, carta):
        if len(self.cartas_trampa) + len(self.cartas_magica) < 3 and isinstance(carta, CartaTrampa):
            self.cartas_trampa.append(carta)
        else:
            print("No hay espacio para más cartas de trampa/mágica en el tablero.")

    def agregar_carta_magica(self, carta):
        if len(self.cartas_trampa) + len(self.cartas_magica) < 3 and isinstance(carta, CartaMagica):
            self.cartas_magica.append(carta)
        else:
            print("No hay espacio para más cartas de trampa/mágica en el tablero.")

