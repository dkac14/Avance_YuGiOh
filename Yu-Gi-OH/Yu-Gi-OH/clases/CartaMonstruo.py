from .Carta import Carta


class CartaMonstruo(Carta):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo, elemento):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo_monstruo = tipo_monstruo
        self.elemento = elemento
        self.en_ataque = True
        self.intento_ataque = True


    def enDefensa(self):
        self.en_ataque = False


    def cambioPosicion(self):
        """Verifica si la carta puede ser jugada directamente (sin sacrificios) basado en el número de estrellas."""
        

    def atacar(self, carta_defensora, oponente):
        from .Jugador import Jugador
        if isinstance(oponente, Jugador):
            if not isinstance(carta_defensora, CartaMonstruo):
                print("No se puede atacar a esta carta, ya que no es un monstruo.")
                return

            if self.en_ataque:
                print(f"{self.nombre} está atacando a {carta_defensora.nombre}.")

                if carta_defensora.en_ataque:
                    if self.ataque > carta_defensora.ataque:
                        print(f"{self.nombre} ha ganado el ataque. {carta_defensora.nombre} ha sido destruida.")
                        self.destruir(oponente.tablero,carta_defensora)     
                        return self.ataque - carta_defensora.ataque
                    elif self.ataque < carta_defensora.ataque:
                        print(f"{self.nombre} ha perdido el ataque. {self.nombre} ha sido destruida.")
                        self.intento_ataque = False
                        return None
                    else:
                        print(f"El ataque de {self.nombre} y {carta_defensora.nombre} es igual. Ninguna carta es destruida.")
                        return None
                else:
                    if self.ataque > carta_defensora.defensa:
                        print(f"{self.nombre} ha destruido a {carta_defensora.nombre}.")
                        oponente.tablero.eliminar_carta(carta_defensora)
                        return self.ataque - carta_defensora.defensa
                    elif self.ataque < carta_defensora.defensa:
                        print(f"{self.nombre} ha fallado el ataque. {carta_defensora.nombre} permanece en el campo.")
                        self.intento_ataque = False
                        return 0
                    else:
                        print(f"El ataque de {self.nombre} es igual a la defensa de {carta_defensora.nombre}. No ocurre nada.")
                        return 0
            else:
                print(f"{self.nombre} no puede atacar porque está en modo defensa.")
    
    def destruir(self, tablero, carta):
        from .Tablero import Tablero
        if (isinstance(tablero, Tablero)):
            tablero.eliminar_carta(carta) 

    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Descripción: {self.descripcion}\n"
            f"Ataque: {self.ataque}\n"
            f"Defensa: {self.defensa}\n"
            f"Tipo de Monstruo: {self.tipo_monstruo}\n"
            f"Elemento: {self.elemento}\n"
        )