from .CartaMonstruo import CartaMonstruo

class Jugador:
    def __init__(self, nombre, deck, tablero):
        self.vida = 4000
        self.nombre = nombre
        self.deck = deck
        self.tablero = tablero
        self.mano = []

    def jugar_turno(self):
        pass

    def robar_carta(self):
        if len(self.deck) > 0:
            carta_robada = self.deck.pop(0)
            self.mano.append(carta_robada)
            print(f"Carta robada: {carta_robada.nombre}")
        else:
            print("No hay cartas en el deck para robar.")

    def cartas_iniciales(self):
        self.mano = self.deck[:5]
        del self.deck[:5]

    def colocar_en_tablero(self, carta):
        if isinstance(carta, CartaMonstruo):
            self.tablero.agregar_carta_monstruo(carta)
        else:
            self.tablero.agregar_carta_trampa_magica(carta)
        if carta in self.mano:
            self.mano.remove(carta)

    def declarar_batalla(self, carta, objetivo, oponente):
        pass
