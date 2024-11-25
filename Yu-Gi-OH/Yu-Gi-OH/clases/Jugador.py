from .CartaMonstruo import CartaMonstruo
from .Tablero import Tablero
from .Carta import Carta
from .CartaMagica import CartaMagica


class Jugador:
    def __init__(self, nombre, deck):
        self.vida = 4000
        self.nombre = nombre
        self.deck = deck
        self.tablero = Tablero()
        self.mano = []

    def jugar_turno(self):
        self.cartas_iniciales()
        print("-----------------------------------------------------")
        print("///////Cartas disponibles de " + self.nombre + ": ///////")
        contador = 1
        for carta in self.mano:
            if isinstance(carta, Carta):
                print(f'({contador})')
                print(carta)
                contador +=1
        print("-----------------------------------------------------")

        carta = input("- Seleccione el número de la carta a colocar: ")
        while not carta.isdigit() or not (1 <= int(carta) <= 5):
            print("Por favor, ingrese un número válido entre 1 y 5.")
            carta = input("- Seleccione el número de la carta a colocar: ")


        self.colocar_en_tablero(self.mano[int(carta) - 1])
        print(self.tablero)
        self.robar_carta()

        lista_cartas = self.tablero.listaCartas()

        for elem in lista_cartas:
            if isinstance(elem, CartaMagica) and elem.sePuedeActivar(lista_cartas):
                entrada = input("Existe una carta Mágica para activarla. Desea activarla? (s/n)")
                while (entrada != "s" and entrada != "n"):
                    entrada = input("Existe una carta Mágica para activarla. Desea activarla? (s/n)")
                if entrada == "s":
                    carta = elem.monstruoActivar()
                    elem.ActivarEfecto(carta)


    def robar_carta(self):
        if len(self.deck) > 0:
            carta_robada = self.deck.pop(0)
            self.mano.append(carta_robada)
            print(f"**** Carta robada: {carta_robada.nombre} ****")
        else:
            print("No hay cartas en el deck para robar.")

    def cartas_iniciales(self):
        self.mano = self.deck[:5]
        del self.deck[:5]

    def colocar_en_tablero(self, carta):
        if isinstance(carta, CartaMonstruo):
            if ( isinstance(self.tablero, Tablero)):
                self.tablero.agregar_carta_monstruo(carta)
                print("- Carta Monstruo agregada.")

        elif isinstance(carta,CartaMagica):
            if (isinstance(self.tablero, Tablero)):
                self.tablero.agregar_carta_magica(carta)
                print("- Carta Magica agregada.")

        else: 
            if (isinstance(self.tablero, Tablero)):
                self.tablero.agregar_carta_trampa(carta)
                print("- Carta Trampa agregada.")

        self.mano.remove(carta)



    def declarar_batalla(self, oponente):
        from .Jugador import Jugador
        if (isinstance(oponente, Jugador)):
            monstruos_jugador = oponente.tablero.obtenerCartasMonstruo()
            if len(monstruos_jugador) == 0:
                print(f"{oponente.nombre} no tiene monstruos en el tablero, ¡realizando un ataque directo a {oponente.nombre}!")
                self.ataque_directo(oponente)
                return

        if (isinstance(oponente, Jugador)):
            if len(self.tablero.obtenerCartasMonstruo()) > 0 :
                n_carta_ataque = input(" - Seleccione la carta para atacar de su tablero: ")

                while not n_carta_ataque.isdigit() or not (1 <= int(n_carta_ataque) <= 6):
                    n_carta_ataque = input("- Seleccione la carta para atacar de su tablero (1-6): ")
            
                carta_atacante = self.tablero.listaCartas()[int(n_carta_ataque) - 1]
                if isinstance(carta_atacante, CartaMonstruo):
                    print("Carta atacante: " + carta_atacante.nombre)
            
                objetivo = input("Seleccione la carta que desea atacar de su oponente (índice): ")

                if objetivo.isdigit() and 1 <= int(objetivo) <= len(oponente.tablero.listaCartas()):
                    cartas_oponente = oponente.tablero.listaCartas()
                    carta_objetivo = cartas_oponente[int(objetivo) - 1]  
                    danio = carta_atacante.atacar(carta_objetivo, cartas_oponente)
                    if carta_atacante.intento_ataque and danio is not None:
                        oponente.vida -= danio
                        print(f"El daño infligido a {oponente.nombre} es de {danio}.")
                    else:
                        self.tablero.eliminar_carta(carta_atacante)
        else:
            print("- No se puede declarar batalla.")


    def ataque_directo(self, oponente):
        if (isinstance(oponente, Jugador)):
            danio = 1000  
            print(f"{self.nombre} ataca directamente a {oponente.nombre} con {danio} puntos de daño.")
            oponente.vida -= danio  
            print(f"La vida de {oponente.nombre} es ahora {oponente.vida}.")
