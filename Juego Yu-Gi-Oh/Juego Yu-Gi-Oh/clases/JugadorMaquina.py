import random
from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa
from .Tablero import Tablero

class JugadorMaquina:
    def __init__(self, nombre, mazo):
        self.nombre = nombre
        self.vida = 4000
        self.mazo = mazo
        self.mano = self.inicializar_mano()
        self.tablero = Tablero()

    def inicializar_mano(self):
        mano_inicial = []
        for _ in range(5):
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
            print("No tienes cartas en tu mano para jugar.")
            return

        print(f"\nCartas en la mano de {self.nombre}:")
        for i, carta in enumerate(self.mano):
            print(f"{i + 1}. {carta.nombre} ({type(carta).__name__}) - {carta.descripcion}")

        # Selección aleatoria de carta
        carta = random.choice(self.mano)

        if isinstance(carta, CartaMonstruo):
            # Modo aleatorio entre 'ataque' o 'defensa'
            modo = random.choice(['ataque', 'defensa'])
            print(f"{self.nombre} juega {carta.nombre} en modo {modo}.")
            if modo == "defensa":
                carta.cambiar_modo()
            if self.tablero.agregar_carta_monstruo(carta):
                print(f"{self.nombre} jugó {carta.nombre} en modo {'ataque' if carta.en_ataque else 'defensa'}.")
        elif isinstance(carta, CartaMagica):
            if not self.tablero.obtener_cartas_monstruo():
                print(f"{self.nombre} no tiene monstruos en el campo para aplicar esta carta mágica.")
                return
            monstruo = random.choice(self.tablero.obtener_cartas_monstruo())  # Selección aleatoria de monstruo
            carta.activar_carta(monstruo)
            print(f"{self.nombre} activó la carta mágica: {carta.nombre} en {monstruo.nombre}.")
            
        elif isinstance(carta, CartaTrampa):
            self.tablero.agregar_carta_magica_o_trampa(carta)
            print(f"{self.nombre} jugó la carta trampa: {carta.nombre} (boca abajo).")

        self.mano.remove(carta)

    def declarar_batalla(self, gamer):

        if self.tablero.turno < 2:
            print("No puedes declarar batalla hasta el segundo turno.")
            self.tablero.turno += 1
            return

        monstruos_atacantes = self.tablero.obtener_cartas_monstruo()
        monstruos_defensores = gamer.tablero.obtener_cartas_monstruo()

        if not monstruos_atacantes:
            print("No tienes monstruos en tu campo para declarar una batalla.")
            return

        monstruos_ya_usados = set()

        while len(monstruos_atacantes) > len(monstruos_ya_usados):
            print("\nMonstruos disponibles para atacar:")
            for i, monstruo in enumerate(monstruos_atacantes):
                if monstruo not in monstruos_ya_usados:
                    print(f"{i + 1}. {monstruo}")

            # Selección aleatoria de atacante
            eleccion_atacante = random.choice([i for i in range(len(monstruos_atacantes)) if monstruos_atacantes[i] not in monstruos_ya_usados])
            carta_atacante = monstruos_atacantes[eleccion_atacante]

            print(f"\n{self.nombre} selecciona {carta_atacante.nombre} para atacar.")

            """# Opciones aleatorias de ataque
            tipo_ataque = random.choice(["1", "2"])

            if tipo_ataque == "1":  # Ataque directo
                print(f"{carta_atacante.nombre} realiza un ataque directo.")
                carta_atacante.recibir_ataque_directo(gamer.vida, carta_atacante.ataque)

            elif tipo_ataque == "2":  # Ataque a un monstruo defensor
                if not monstruos_defensores:
                    print(f"{self.nombre} no tiene monstruos defensores, realizando un ataque directo.")
                    continue

                # Selección aleatoria de defensor
                carta_defensora = random.choice(monstruos_defensores)
                carta_atacante.atacar(carta_defensora, gamer.tablero.obtener_cartas_trampa(), gamer.vida, monstruos_defensores, monstruos_atacantes)

            monstruos_ya_usados.add(carta_atacante)

            continuar = random.choice(["sí", "no"])
            if continuar != "sí":
                print(f"{self.nombre} ha terminado su fase de batalla.")
                break"""