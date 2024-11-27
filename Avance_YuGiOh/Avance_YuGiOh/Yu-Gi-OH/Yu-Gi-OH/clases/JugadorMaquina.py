import random
from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa

class JugadorMaquina:
    def __init__(self, nombre, mazo):
        from .Tablero import Tablero
        self.nombre = nombre
        self.vida = 4000
        self.mazo = mazo
        self.mano = self.inicializar_mano()
        self.tablero = Tablero()

    def inicializar_mano(self):
        mano_inicial = []
        for _ in range(4):
            if self.mazo:
                mano_inicial.append(self.mazo.pop(0))
        return mano_inicial

    def robar_carta(self):
        if self.mazo:
            carta = self.mazo.pop(0)
            self.mano.append(carta)
            print(f"{self.nombre} robó la carta: {carta.nombre}")
        else:
            print(f"{self.nombre} no tiene más cartas en el mazo.")

    def jugar_carta(self):
        if not self.mano:
            print(f"{self.nombre} no tiene cartas en su mano para jugar.")
            return

        carta = random.choice(self.mano)

        if isinstance(carta, CartaMonstruo):
            modo = random.choice(["ataque", "defensa"])
            if modo == "defensa":
                carta.cambiar_modo()

            if self.tablero.agregar_carta_monstruo(carta):
                print(f"{self.nombre} jugó {carta.nombre} en modo {'ataque' if carta.en_ataque else 'defensa'}.")

        elif isinstance(carta, CartaMagica):
            if not self.tablero.obtener_cartas_monstruo():
                print("No hay monstruos en el campo para aplicar esta carta mágica.")
                return

            encontro = 0
            # Recorre las cartas monstruo en el tablero.
            for monstruo in self.tablero.obtener_cartas_monstruo():
                # Verifica si el tipo de monstruo coincide con el tipo de la carta mágica.
                if monstruo.tipo_monstruo == carta.tipo_monstruo:
                    # Activa la carta mágica en el monstruo y actualiza el atributo correspondiente.
                    if carta.tipo_incremento == "ataque":
                        carta.ataque = carta.activar_carta(monstruo)  # Actualiza el ataque del monstruo.
                    elif carta.tipo_incremento == "defensa":
                        carta.defensa = carta.activar_carta(monstruo)  # Actualiza la defensa del monstruo.

                    # Agrega la carta mágica al tablero tras la activación.
                    self.tablero.agregar_carta_magica_o_trampa(carta)
                    encontro = 1
                    print(f"{monstruo.nombre} equipado con {carta.nombre}.")

            # Si no se encontró un monstruo compatible.
            if encontro == 0:
                print("No hay monstruos de este tipo en el campo para aplicar esta carta mágica.")
            
        elif isinstance(carta, CartaTrampa):
            self.tablero.agregar_carta_magica_o_trampa(carta)
            print(f"{self.nombre} jugó la carta trampa {carta.nombre} (boca abajo).")

        self.mano.remove(carta)

    def declarar_batalla(self, gamer):
        if self.tablero.turno < 2:
            print(f"{self.nombre} no puede declarar batalla hasta el segundo turno.")
            self.tablero.turno += 1
            return

        monstruos_atacantes = self.tablero.obtener_cartas_monstruo()
        monstruos_defensores = gamer.tablero.obtener_cartas_monstruo()

        if not monstruos_atacantes:
            print(f"{self.nombre} no tiene monstruos en su campo para declarar una batalla.")
            return

        monstruos_ya_usados = set()

        while len(monstruos_atacantes) > len(monstruos_ya_usados):
            # Seleccionar monstruo atacante aleatoriamente que no haya atacado aún
            carta_atacante = random.choice([m for m in monstruos_atacantes if m not in monstruos_ya_usados])

            # Decidir tipo de ataque: directo (1) o a un defensor (2)
            if monstruos_defensores and random.choice([1, 2]) == 2:  # Ataque a defensor
                carta_defensora = random.choice(monstruos_defensores)
                gamer.vida = carta_atacante.atacar(
                    carta_defensora,
                    gamer.vida,
                    self.vida,
                    monstruos_atacantes.index(carta_atacante),
                    monstruos_defensores.index(carta_defensora),
                    self.tablero,
                    gamer.tablero,
                )
                print(f"{self.nombre} atacó a {carta_defensora.nombre} con {carta_atacante.nombre}.")
            else:  # Ataque directo
                if monstruos_defensores:
                    print(f"{self.nombre} no puede realizar un ataque directo porque hay monstruos defensores.")
                else:
                    gamer.vida = carta_atacante.recibir_ataque_directo(gamer.vida, carta_atacante.ataque, gamer.tablero)
                    print(f"{self.nombre} realizó un ataque directo con {carta_atacante.nombre}.")

            # Marcar el monstruo como usado
            monstruos_ya_usados.add(carta_atacante)

            # Si todos los monstruos han atacado, termina la fase
            if len(monstruos_ya_usados) == len(monstruos_atacantes):
                print(f"{self.nombre} ha terminado la fase de batalla.")
                break
