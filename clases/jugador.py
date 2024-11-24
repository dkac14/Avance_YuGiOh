class Jugador:
    def __init__(self, nombre, deck):
        self.nombre = nombre
        self.vida = 4000
        self.deck = deck
        self.mano = self.iniciar_mano()
        #self.tablero = Tablero()

    def iniciar_mano(self):
        mano_inicial = [self.deck.robar() for _ in range(5)]
        return mano_inicial

    def robar_carta(self):
        carta = self.deck.robar()
        if carta:
            self.mano.append(carta)
            print(f"{self.nombre} ha robado una carta: {carta.nombre}")
        else:
            print(f"{self.nombre} no tiene más cartas en el deck.")

    def jugar_carta(self, carta, posicion, tipo, ataque=True):
        if tipo == "monstruo":
            self.tablero.colocar_carta(carta, posicion, tipo, ataque)
        elif tipo == "magica_trampa":
            self.tablero.colocar_carta(carta, posicion, tipo)
        self.mano.remove(carta)
        print(f"{self.nombre} ha jugado la carta: {carta.nombre}")

    def cambiar_posicion(self, posicion):
        self.tablero.cambiar_posicion(posicion)
        print(f"{self.nombre} ha cambiado la posición de la carta en la posición {posicion}")

    def __str__(self):
        return f"Jugador: {self.nombre}, Puntos: {self.vida}, Mano: {[carta.nombre for carta in self.mano]}"