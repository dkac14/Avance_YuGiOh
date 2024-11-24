from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa
import numpy as np

class Tablero:
    def __init__(self):
        self.turno = 1
        self.tablero_monstruos = [None] * 3  # Tres espacios para monstruos
        self.tablero_magicas_trampas = [None] * 3  # Tres espacios para mágicas/trampas

    def agregar_carta_monstruo(self, carta):
        if isinstance(carta, CartaMonstruo):
            for i in range(3):
                if self.tablero_monstruos[i] is None:
                    self.tablero_monstruos[i] = carta
                    return True
            print("No hay espacio para más cartas de monstruo en el tablero.")
        return False

    def agregar_carta_trampa(self, carta):
        if isinstance(carta, CartaTrampa):
            for i in range(3):
                if self.tablero_magicas_trampas[i] is None:
                    self.tablero_magicas_trampas[i] = carta
                    return True
            print("No hay espacio para más cartas trampa en el tablero.")
        return False

    def agregar_carta_magica(self, carta):
        if isinstance(carta, CartaMagica):
            for i in range(3):
                if self.tablero_magicas_trampas[i] is None:
                    self.tablero_magicas_trampas[i] = carta
                    return True
            print("No hay espacio para más cartas mágicas en el tablero.")
        return False

    def obtener_cartas_monstruo(self):
        return [carta for carta in self.tablero_monstruos if carta]

    def obtener_cartas_magicas(self):
        return [carta for carta in self.tablero_magicas_trampas if isinstance(carta, CartaMagica)]

    def obtener_cartas_trampa(self):
        return [carta for carta in self.tablero_magicas_trampas if isinstance(carta, CartaTrampa)]

    def eliminar_carta(self, carta):
        if carta in self.tablero_monstruos:
            self.tablero_monstruos[self.tablero_monstruos.index(carta)] = None
        elif carta in self.tablero_magicas_trampas:
            self.tablero_magicas_trampas[self.tablero_magicas_trampas.index(carta)] = None
