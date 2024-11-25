import random
from .Jugador import Jugador
from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica


class JugadorMaquina(Jugador):
    def __init__(self, nombre, deck):
        super().__init__(nombre, deck)

    def jugar_turno(self):
        print(f"\n{self.nombre} (Máquina) está jugando.")
        self.cartas_iniciales()
        self.colocar_carta_aleatoria_en_tablero()
        self.robar_carta()
        print(self.tablero)
        lista_cartas = self.tablero.listaCartas()
        for elem in lista_cartas:
            if isinstance(elem, CartaMagica) and elem.sePuedeActivar(lista_cartas):
                carta = elem.monstruoActivar(lista_cartas)
                elem.ActivarEfecto(carta)



    def colocar_carta_aleatoria_en_tablero(self):
        if len(self.mano) > 0:
            carta_a_colocar = random.choice(self.mano)  
            print(f"{self.nombre} coloca la carta: {carta_a_colocar.nombre}")
            self.colocar_en_tablero(carta_a_colocar)


    def realizar_ataque(self):
        monstruos_en_tablero = self.tablero.obtenerCartasMonstruo()

        if monstruos_en_tablero:
            carta_atacante = random.choice(monstruos_en_tablero) 
            print(f"{self.nombre} ataca con: {carta_atacante.nombre}")
        else:
            print(f"{self.nombre} no tiene monstruos en el tablero para atacar.")


    def declarar_batalla(self, oponente):
        if len(self.tablero.obtenerCartasMonstruo()) > 0 :
            monstruos_en_tablero = self.tablero.obtenerCartasMonstruo()
            carta_atacante = random.choice(monstruos_en_tablero) 

            if (isinstance(oponente, Jugador)):
                cartas_oponente = oponente.tablero.listaCartas()

            if isinstance(carta_atacante, CartaMonstruo):
                print("Carta atacante: " + carta_atacante.nombre)
            
            carta_objetivo = None
            for carta in cartas_oponente:
                if (isinstance(carta, CartaMonstruo)):
                    carta_objetivo = carta
            
            danio = carta_atacante.atacar(carta_objetivo, oponente)
            if danio is not None:
                if carta_atacante.intento_ataque:
                    oponente.vida -= danio
                    print(f"El daño infligido a {oponente.nombre} es de {danio}.")
                
        else:
            print("- No se puede declarar batalla.")



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