from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa
import numpy as np

class Tablero:
    def __init__(self):
        # Espacios de cartas: 3 para monstruos y 3 para mágicas/trampa
        self.zona_monstruos = [None] * 3
        self.zona_magica_trampa = [None] * 3
        self.turno = 1

    def agregar_carta_monstruo(self, carta):
        """
        Agrega una carta monstruo a la zona de monstruos.
        """
        if isinstance(carta, CartaMonstruo):
            for i in range(len(self.zona_monstruos)):
                if self.zona_monstruos[i] is None:
                    self.zona_monstruos[i] = carta
                    print(f"Carta {carta.nombre} colocada en la zona de monstruos en modo {'ataque' if carta.en_ataque else 'defensa'}.")
                    return True
        print("No hay espacio disponible en la zona de monstruos.")
        return False

    def agregar_carta_magica_o_trampa(self, carta):
        """
        Agrega una carta mágica o de trampa a la zona correspondiente.
        """
        if isinstance(carta, (CartaMagica, CartaTrampa)):
            for i in range(len(self.zona_magica_trampa)):
                if self.zona_magica_trampa[i] is None:
                    self.zona_magica_trampa[i] = carta
                    estado = "boca abajo" if isinstance(carta, CartaTrampa) else "boca arriba"
                    print(f"Carta {carta.nombre} colocada en la zona de mágicas/trampa ({estado}).")
                    return True
        print("No hay espacio disponible en la zona de mágicas/trampa.")
        return False

    def obtener_cartas_monstruo(self):
        """
        Devuelve las cartas de la zona de monstruos.
        """
        return [carta for carta in self.zona_monstruos if carta is not None]

    def obtener_cartas_magicas(self):
        """
        Devuelve las cartas mágicas de la zona mágica/trampa.
        """
        return [carta for carta in self.zona_magica_trampa if isinstance(carta, CartaMagica)]

    def obtener_cartas_trampa(self):
        """
        Devuelve las cartas trampa de la zona mágica/trampa.
        """
        return [carta for carta in self.zona_magica_trampa if isinstance(carta, CartaTrampa)]

    def mostrar_tablero_1(self, jugador, enemigo):
        from .Jugador import Jugador
        from .JugadorMaquina import JugadorMaquina

        """
        Muestra las cartas actuales en el tablero con un diseño mucho más grande.
        Este es el tablero de la persona (jugador).
        """
        MounstroZone = []
        for i, carta in enumerate(self.zona_monstruos):
            if carta and carta.en_ataque:
                MounstroZone.append(f"[{i + 1}] {carta}")
            elif carta:
                MounstroZone.append(f"[{i + 1}] Carta en modo defensa (boca abajo)")
            else:
                MounstroZone.append(f"[{i + 1}] (vacío)")

        MagicasTrampaZone = []
        for i, carta in enumerate(self.zona_magica_trampa):
            if carta:
                estado = "boca arriba" if not isinstance(carta, CartaTrampa) or not carta.boca_abajo else "boca abajo"
                MagicasTrampaZone.append(f"[{i + 1}] {carta} - ({estado})")
            else:
                MagicasTrampaZone.append(f"[{i + 1}] (vacío)")
            
            # Crear las zonas de cartas con numpy
        tablero = np.array([
            ["**Zona Monstruos**", *MounstroZone],  # Zona de Monstruos
            ["**Zona Mágica y Trampa**", *MagicasTrampaZone]  # Zona de Magia y Trampa
        ], dtype=object)

        # Definir el ancho de cada celda para alinearlo bien
        max_len = 30  # Ancho máximo para cada celda, ajustable según sea necesario

        # Imprimir el tablero de manera bonita con el título centrado
        print("-" * (max_len * 5))  # Línea superior para separar el tablero
        for i, row in enumerate(tablero):
            # Centrar los títulos
            if i == 0:  # Si es la primera fila (Zona Monstruos)
                print(f"{row[0]:^{max_len * 5}}")  # Centrado del título de la zona de monstruos
            elif i == 1:  # Si es la segunda fila (Zona Mágica y Trampa)
                print(f"{row[0]:^{max_len * 5}}")  # Centrado del título de la zona de magia y trampa
            # Imprimir las cartas alineadas
            print(" | ".join([str(cell).ljust(max_len) for cell in row[1:]]))  # Mostrar las cartas alineadas
            print("-" * (max_len * 5))  # Línea inferior para separar las cartas
        
        
        if isinstance(jugador, Jugador) and isinstance(enemigo, JugadorMaquina):
            print(" ")
        return f"Gil 1: {jugador.vida}   Gil 2: {enemigo.vida}\n" 
                
        

    def mostrar_tablero_2(self):
        """
        Muestra las cartas actuales en el tablero con un diseño mucho más grande.
        Este es el tablero del enemigo.
        """
        MounstroZone = []
        for i, carta in enumerate(self.zona_monstruos):
            if carta and carta.en_ataque:
                MounstroZone.append(f"[{i + 1}] {carta}")
            elif carta:
                MounstroZone.append(f"[{i + 1}] Carta en modo defensa (boca abajo)")
            else:
                MounstroZone.append(f"[{i + 1}] (vacío)")

        MagicasTrampaZone = []
        for i, carta in enumerate(self.zona_magica_trampa):
            if carta:
                estado = "boca arriba" if not isinstance(carta, CartaTrampa) or not carta.boca_abajo else "boca abajo"
                MagicasTrampaZone.append(f"[{i + 1}] {carta} - ({estado})")
            else:
                MagicasTrampaZone.append(f"[{i + 1}] (vacío)")

        # Crear las zonas de cartas con numpy
        tablero = np.array([
            ["**Zona Mágica y Trampa**", *MagicasTrampaZone],  # Zona de Magia y Trampa
            ["**Zona Monstruos**", *MounstroZone]  # Zona de Monstruos
        ], dtype=object)

        # Definir el ancho de cada celda para alinearlo bien
        max_len = 30  # Ancho máximo para cada celda, ajustable según sea necesario

        # Imprimir el tablero de manera bonita con el título centrado
        print("-" * (max_len * 5))  # Línea superior para separar el tablero
        for i, row in enumerate(tablero):
            # Centrar los títulos
            if i == 0:  # Si es la primera fila (Zona Monstruos)
                print(f"{row[0]:^{max_len * 5}}")  # Centrado del título de la zona de monstruos
            elif i == 1:  # Si es la segunda fila (Zona Mágica y Trampa)
                print(f"{row[0]:^{max_len * 5}}")  # Centrado del título de la zona de magia y trampa
            # Imprimir las cartas alineadas
            print(" | ".join([str(cell).ljust(max_len) for cell in row[1:]]))  # Mostrar las cartas alineadas
            print("-" * (max_len * 5))  # Línea inferior para separar las cartas
            
            
        return " "

    def eliminar_carta_monstruo(self, indice):
        """
        Elimina una carta monstruo de la zona de monstruos.
        """
        if 0 <= indice < len(self.zona_monstruos) and self.zona_monstruos[indice]:
            carta_eliminada = self.zona_monstruos[indice]
            self.zona_monstruos[indice] = None
            print(f"Carta {carta_eliminada.nombre} eliminada de la zona de monstruos.")
            return carta_eliminada
        print("No hay carta en la posición indicada.")
        return None

    def eliminar_carta_magica_trampa(self, indice):
        """
        Elimina una carta mágica o trampa de la zona correspondiente.
        """
        if 0 <= indice < len(self.zona_magica_trampa) and self.zona_magica_trampa[indice]:
            carta_eliminada = self.zona_magica_trampa[indice]
            self.zona_magica_trampa[indice] = None
            print(f"Carta {carta_eliminada.nombre} eliminada de la zona de mágicas/trampa.")
            return carta_eliminada
        print("No hay carta en la posición indicada.")
        return None