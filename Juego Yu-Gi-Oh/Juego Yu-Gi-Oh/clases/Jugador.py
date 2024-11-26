from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa
from .Tablero import Tablero

class Jugador:
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

        print("Cartas en tu mano:")
        for i, carta in enumerate(self.mano):
            print(f"{i + 1}. {carta.nombre} ({type(carta).__name__}) - {carta.descripcion}")

        eleccion = -1
        while eleccion < 0 or eleccion >= len(self.mano):
            entrada = input("Selecciona el número de la carta que deseas jugar: ")
            if entrada.isdigit():
                eleccion = int(entrada) - 1
            else:
                print("Entrada no válida. Por favor, introduce un número.")

        carta = self.mano[eleccion]

        if isinstance(carta, CartaMonstruo):
            modo = input("¿En qué modo quieres jugar la carta? (ataque/defensa): ").strip().lower()
            while modo not in ["ataque", "defensa"]:
                modo = input("¿En qué modo quieres jugar la carta? (ataque/defensa): ").strip().lower()
                if modo not in ["ataque", "defensa"]:
                    print("Opción inválida. Por favor, ingresa 'ataque' o 'defensa'.")
            if modo == "defensa":
                carta.cambiar_modo()
            print(f"{carta.en_ataque}")
            if self.tablero.agregar_carta_monstruo(carta):
                print(f"Jugaste {carta.nombre} en modo {'ataque' if carta.en_ataque else 'defensa'}.")
        elif isinstance(carta, CartaMagica):
            if not self.tablero.obtener_cartas_monstruo():
                print("No hay monstruos en el campo para aplicar esta carta mágica.")
                return
            print("Selecciona el monstruo al que deseas aplicar el efecto:")
            
            for i, monstruo in enumerate(self.tablero.obtener_cartas_monstruo()):
                print(f"{i + 1}. {monstruo.nombre} (ATK: {monstruo.ataque}, DEF: {monstruo.defensa})")
            
            seleccion_monstruo = -1
            while seleccion_monstruo < 0 or seleccion_monstruo >= len(self.tablero.obtener_cartas_monstruo()):
                entrada = input("Selecciona el número del monstruo: ")
                if entrada.isdigit():
                    seleccion_monstruo = int(entrada) - 1
            monstruo = self.tablero.obtener_cartas_monstruo()[seleccion_monstruo]
            carta.activar_carta(monstruo)  # Activa la carta mágica en el monstruo
            
        elif isinstance(carta, CartaTrampa):
            self.tablero.agregar_carta_magica_o_trampa(carta)  
            print(f"Jugaste la carta trampa: {carta.nombre} (boca abajo).")

        self.mano.remove(carta)

    def declarar_batalla(self, gamer):

        print(f"Tu tablero: {self.tablero.mostrar_tablero()}")
        print(f"Tu tablero: {gamer.tablero.mostrar_tablero()}")

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

            eleccion_atacante = int(input("Selecciona el número del monstruo atacante (o 0 para salir): ")) - 1
            if eleccion_atacante == -1:
                print("Terminaste la fase de batalla.")
                break

            if eleccion_atacante < 0 or eleccion_atacante >= len(monstruos_atacantes):
                print("Selección inválida. Intenta nuevamente.")
                continue

            carta_atacante = monstruos_atacantes[eleccion_atacante]
            if carta_atacante in monstruos_ya_usados:
                print(f"{carta_atacante.nombre} ya atacó este turno.")
                continue

            print("\nOpciones de ataque:")
            print("1. Ataque directo al jugador.")
            print("2. Ataque a un monstruo defensor.")
            tipo_ataque = input("Elige el tipo de ataque: ").strip()

            if tipo_ataque == "1":  # Ataque directo
                if len(monstruos_defensores) > 0:
                    print("El oponente tiene monstruos en el campo.")
                    continue
                else:
                    print(f"{carta_atacante.nombre} realiza un ataque directo.")
                    carta_atacante.recibir_ataque_directo(gamer.vida, carta_atacante.ataque)

            elif tipo_ataque == "2":  # Ataque a un monstruo defensor
                if not monstruos_defensores:
                    print("El oponente no tiene monstruos en el campo. Realiza un ataque directo.")
                    continue

                print("Monstruos defensores disponibles:")
                for i, defensor in enumerate(monstruos_defensores):
                    print(f"{i + 1}. {defensor}")

                eleccion_defensor = int(input("Selecciona el número del monstruo defensor: ")) - 1
                if eleccion_defensor < 0 or eleccion_defensor >= len(monstruos_defensores):
                    print("Selección inválida. Intenta nuevamente.")
                    continue

                carta_defensora = monstruos_defensores[eleccion_defensor]
                carta_atacante.atacar(carta_defensora, gamer.tablero.obtener_cartas_trampa(), gamer.vida, monstruos_defensores, monstruos_atacantes)

            else:
                print("Opción inválida. Intenta nuevamente.")
                continue

            monstruos_ya_usados.add(carta_atacante)
            continuar = input("¿Deseas continuar atacando? (sí/no): ").strip().lower()
            while continuar != "sí" and continuar != "no":
                print("Respuesta inválida. Por favor, responde con 'sí' o 'no'.")
                continuar = input("¿Deseas continuar atacando? (sí/no): ").strip().lower()

            if continuar == "no":
                print("Terminaste la fase de batalla.")
                break
