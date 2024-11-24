from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa
import numpy as np

class Tablero:
    def __init__(self):
        self.tablero = np.full((2, 3), None)
        self.cartas_monstruo = 0
        self.cartas_Magica_Trampa = 0

    def agregar_carta_monstruo(self, carta):
        if self.cartas_monstruo < 3 and isinstance(carta, CartaMonstruo):
            for fila in range(2):  
                for columna in range(3):  
                    if self.tablero[fila][columna] is None:  
                        self.tablero[fila][columna] = carta  
                        self.cartas_monstruo += 1
                        return 
            print("No hay espacio para más cartas de monstruo en el tablero.")

    def agregar_carta_trampa(self, carta):
        if self.cartas_Magica_Trampa < 3 and isinstance(carta, CartaTrampa):
            for fila in range(2):  
                for columna in range(3):  
                    if self.tablero[fila][columna] is None:  
                        self.tablero[fila][columna] = carta  
                        self.cartas_Magica_Trampa += 1
                        return 
            print("No hay espacio para más cartas de trampa/mágica en el tablero.")

    def agregar_carta_magica(self, carta):
        if self.cartas_Magica_Trampa < 3 and isinstance(carta, CartaMagica):
            for fila in range(2):  
                for columna in range(3):  
                    if self.tablero[fila][columna] is None:  
                        self.tablero[fila][columna] = carta  
                        self.cartas_Magica_Trampa += 1
                        return 
            print("No hay espacio para más cartas de trampa/mágica en el tablero.")


    def obtenerCartasTrampa(self):
        trampas = []
        for fila in range(2):  
            for columna in range(3):  
                if isinstance(self.tablero[fila][columna], CartaTrampa):
                    trampas.append(self.tablero[fila][columna])
        return trampas
    

    def obtenerCartasMágicas(self):
        magicas = []
        for fila in range(2):  
            for columna in range(3):  
                if isinstance(self.tablero[fila][columna], CartaMagica):
                    magicas.append(self.tablero[fila][columna])
        return magicas 