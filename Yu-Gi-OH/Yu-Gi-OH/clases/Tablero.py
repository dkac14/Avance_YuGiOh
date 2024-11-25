from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa
from .Carta import Carta
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
    
    def obtenerCartasMonstruo(self):
        monstruos = []
        for fila in range(2):  
            for columna in range(3):  
                if isinstance(self.tablero[fila][columna], CartaMonstruo):
                    monstruos.append(self.tablero[fila][columna])
        return monstruos

    def obtenerCartasMágicas(self):
        magicas = []
        for fila in range(2):  
            for columna in range(3):  
                if isinstance(self.tablero[fila][columna], CartaMagica):
                    magicas.append(self.tablero[fila][columna])
        return magicas 
    

    def listaCartas(self):
        cartas = []
        for fila in range(2):  
            for columna in range(3):  
                    cartas.append(self.tablero[fila][columna])
        return cartas

    def __str__(self):
        resultado = ""  
        contador = 1
        for fila in range(len(self.tablero)): 
            for columna in range(len(self.tablero[fila])):  
                carta = self.tablero[fila][columna]
                if carta is not None and isinstance(carta, Carta):  
                    resultado += f"[({contador}) {carta.nombre}        ]"  
                else:  
                    resultado += f"[({contador})        Vacío             ]"
                contador += 1  
            resultado += "\n"  
        return resultado
    

    def eliminar_carta(self, carta):
        for fila in range(2):  
            for columna in range(3):  
                if self.tablero[fila][columna] == carta:
                    self.tablero[fila][columna] = None  
                    if isinstance(carta, CartaMonstruo):
                        self.cartas_monstruo -= 1
                    elif isinstance(carta, (CartaMagica, CartaTrampa)):
                        self.cartas_Magica_Trampa -= 1
                    print(f"La carta {carta.nombre} ha sido eliminada del tablero.")
                    return
                
    
    