from classes.CartaMagica import CartaMagica
from classes.CartaMonstruo import CartaMonstruo
from classes.CartaTrampa import CartaTrampa

class Tablero:
    def __init__(self):
        # Espacios de cartas: 3 para monstruos y 3 para mágicas/trampa
        self.zona_monstruos = [None] * 3
        self.zona_magica_trampa = [None] * 3

    def agregar_carta_monstruo(self, carta, modo_ataque=True):
        """
        Agrega una carta monstruo a la zona de monstruos.
        """
        if isinstance(carta, CartaMonstruo):
            for i in range(len(self.zona_monstruos)):
                if self.zona_monstruos[i] is None:
                    carta.en_ataque = modo_ataque
                    self.zona_monstruos[i] = carta
                    print(f"Carta {carta.nombre} colocada en la zona de monstruos en modo {'ataque' if modo_ataque else 'defensa'}.")
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

    def mostrar_tablero(self):
        """
        Muestra las cartas actuales en el tablero.
        """
        print("\nZona de monstruos:")
        for i, carta in enumerate(self.zona_monstruos):
            if carta:
                print(f"{i + 1}. {carta} - {'Ataque' if carta.en_ataque else 'Defensa'}")
            else:
                print(f"{i + 1}. (vacío)")

        print("\nZona de mágicas/trampa:")
        for i, carta in enumerate(self.zona_magica_trampa):
            if carta:
                estado = "boca arriba" if not isinstance(carta, CartaTrampa) or not carta.boca_abajo else "boca abajo"
                print(f"{i + 1}. {carta} - ({estado})")
            else:
                print(f"{i + 1}. (vacío)")

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
