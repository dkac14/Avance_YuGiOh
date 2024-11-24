import random
from clases.jugador import Jugador
from clases.CartaMonstruo import CartaMonstruo
from clases.CartaMagica import CartaMagica
from clases.CartaTrampa import CartaTrampa

class JugadorMaquina(Jugador):
    def __init__(self, nombre, mazo):
        super().__init__(nombre, mazo)

    def jugar_carta(self):
        if not self.mano:
            print(f"{self.nombre} no tiene cartas en la mano para jugar.")
            return

        carta = random.choice(self.mano)

        if isinstance(carta, CartaMonstruo):
            modo = random.choice(["ataque", "defensa"])
            if modo == "defensa":
                carta.cambiar_modo()
            if self.tablero.agregar_carta_monstruo(carta):
                print(f"{self.nombre} jugó {carta.nombre} en modo {'ataque' if carta.en_ataque else 'defensa'}.")
        elif isinstance(carta, CartaMagica):
            monstruos = self.tablero.obtenerCartasMonstruo()
            if monstruos:
                objetivo = random.choice(monstruos)
                carta.activar_carta(objetivo)
                print(f"{self.nombre} activó la carta mágica {carta.nombre} sobre {objetivo.nombre}.")
            else:
                print(f"{self.nombre} no pudo activar {carta.nombre} porque no hay objetivos.")
        elif isinstance(carta, CartaTrampa):
            self.tablero.agregar_carta_trampa(carta)
            print(f"{self.nombre} colocó una carta trampa boca abajo: {carta.nombre}.")

        self.mano.remove(carta)

    def declarar_batalla(self):
        monstruos_atacantes = self.tablero.obtener_cartas_monstruo()
        monstruos_defensores = self.tablero.obtener_cartas_monstruo(oponente=True)

        if not monstruos_atacantes:
            print(f"{self.nombre} no tiene monstruos para declarar batalla.")
            return

        for carta_atacante in monstruos_atacantes:
            if monstruos_defensores:
                carta_defensora = random.choice(monstruos_defensores)
                self.tablero.oponente.vida = carta_atacante.atacar(carta_defensora, [], self.tablero.oponente.vida)
                print(f"{self.nombre} atacó a {carta_defensora.nombre} con {carta_atacante.nombre}.")
            else:
                self.tablero.oponente.vida = carta_atacante.atacar(None, [], self.tablero.oponente.vida)
                print(f"{self.nombre} realizó un ataque directo con {carta_atacante.nombre}.")
