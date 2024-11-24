from .Tablero import Tablero
from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa

class Jugador:
    def __init__(self, nombre, mazo):
        self.nombre = nombre
        self.vida = 4000
        self.mazo = mazo
        self.mano = self.inicializar_mano() 
        self.tablero = Tablero()
        self.turno = 1  

    # Para generar las primeras 5 cartas del mazo
    def inicializar_mano(self):
        mano_inicial = []
        for _ in range(5):
            if self.mazo:
                mano_inicial.append(self.mazo.pop(0))
        return mano_inicial

    # Roba carta por cada turno del mazo
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
        
        # Muestra cartas disponibles
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

        # Verifica que tipo de carta es y la coloca en el tablero
        if isinstance(carta, CartaMonstruo):
            modo = input("¿En qué modo quieres jugar la carta? (ataque/defensa): ").strip().lower()
            modo = "ataque" if modo != "defensa" else "defensa"
            carta.en_ataque = modo == "ataque"
            self.tablero.agregar_carta_monstruo(carta)  
            print(f"Jugaste la carta de monstruo: {carta.nombre} en modo {modo}.")
            
        elif isinstance(carta, CartaMagica):
            if not self.tablero.obtenerCartasMonstruo():
                print("No hay monstruos en el campo para aplicar esta carta mágica.")
                return
            print("Selecciona el monstruo al que deseas aplicar el efecto:")
            
            for i, monstruo in enumerate(self.tablero.obtenerCartasMonstruo()):
                print(f"{i + 1}. {monstruo.nombre} (ATK: {monstruo.ataque}, DEF: {monstruo.defensa})")
            
            seleccion_monstruo = -1
            while seleccion_monstruo < 0 or seleccion_monstruo >= len(self.tablero.obtenerCartasMonstruo()):
                entrada = input("Selecciona el número del monstruo: ")
                if entrada.isdigit():
                    seleccion_monstruo = int(entrada) - 1
            monstruo = self.tablero.obtenerCartasMonstruo()[seleccion_monstruo]
            carta.activar_carta(monstruo)  # Activa la carta mágica en el monstruo
            
        elif isinstance(carta, CartaTrampa):
            self.tablero.agregar_carta_trampa(carta)  
            print(f"Jugaste la carta trampa: {carta.nombre} (boca abajo).")

        self.mano.remove(carta)

    #Cambia la posicion uwu
    def cambiar_posicion(self, carta):
        if isinstance(carta, CartaMonstruo) and carta in self.tablero.tablero:
            if carta.en_ataque is not None:  
                carta.en_ataque = not carta.en_ataque
                modo = "ataque" if carta.en_ataque else "defensa"
                print(f"La carta {carta.nombre} ahora está en modo {modo}.")
            else:
                print("La carta no tiene un modo válido.")
        else:
            print("No puedes cambiar la posición de esta carta.")



    def declarar_batalla(self, carta_atacante, carta_defensora=None):
        if self.turno < 2:
            print("No puedes declarar batalla hasta el segundo turno.")
            return

        if carta_atacante not in self.tablero.obtenerCartasMonstruo():
            print("La carta atacante no está en tu tablero.")
            return

        if carta_defensora and carta_defensora not in self.tablero.obtenerCartasMonstruo():
            print("La carta defensora no está en el tablero del oponente.")
            return

        if carta_defensora:
            if carta_atacante.ataque > carta_defensora.defensa:
                print(f"{carta_atacante.nombre} destruyó a {carta_defensora.nombre}.")
            elif carta_atacante.ataque < carta_defensora.defensa:
                print(f"{carta_atacante.nombre} fue destruida en el ataque.")
            else:
                print("Ambas cartas se destruyen.")
        else:
            print(f"{carta_atacante.nombre} realizó un ataque directo al oponente.")
