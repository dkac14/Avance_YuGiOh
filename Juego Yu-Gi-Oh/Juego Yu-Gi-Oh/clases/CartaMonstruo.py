from .Carta import Carta
from .CartaTrampa import CartaTrampa

class CartaMonstruo(Carta):

    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo, elemento, modo):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo_monstruo = tipo_monstruo
        self.elemento = elemento
        self.en_ataque = modo

    # Métodos principales
    def atacar(self, carta_defensora, lista_cartas_trampa, puntos_vida_oponente, lista_cartas_defensora, lista_cartas_atacante):
        """
        Ataca a una carta defensora. Verifica cartas trampa y calcula daño según el modo de las cartas.
        """
        if carta_defensora == None:
            puntos_vida_oponente = puntos_vida_oponente - self.ataque
            return puntos_vida_oponente
        
        elif not isinstance(carta_defensora, CartaMonstruo):
            print(f"{self.nombre} no puede atacar a la carta, ya que no es un monstruo.")
            return puntos_vida_oponente

        print(f"{self.nombre} declara un ataque a {carta_defensora.nombre}.")

        # Verificar cartas trampa
        for carta_trampa in lista_cartas_trampa:
            if isinstance(carta_trampa, CartaTrampa) and carta_trampa.verificar(self):
                carta_trampa.activar(self, lista_cartas_trampa)
                return puntos_vida_oponente
 
        # Continuar con el ataque si no hay trampas activadas
        if self.en_ataque:
            if carta_defensora.en_ataque:
                # Ataque vs. Ataque
                if self.ataque > carta_defensora.ataque:
                    print(f"{self.nombre} destruye a {carta_defensora.nombre}.")
                    carta_defensora.destruir(lista_cartas_defensora, carta_defensora.nombre)
                    puntos_vida_oponente -= (self.ataque - carta_defensora.ataque)
                elif self.ataque < carta_defensora.ataque:
                    print(f"{self.nombre} es destruido por {carta_defensora.nombre}.")
                    self.destruir(lista_cartas_atacante)
                else:
                    print(f"El ataque termina en empate. Ningún monstruo es destruido.")
            else:
                # Ataque vs. Defensa
                if self.ataque > carta_defensora.defensa:
                    print(f"{self.nombre} destruye a {carta_defensora.nombre} en modo defensa.")
                    carta_defensora.destruir(lista_cartas_defensora)
                elif self.ataque < carta_defensora.defensa:
                    dano = carta_defensora.defensa - self.ataque
                    puntos_vida_oponente -= dano
                    print(f"{self.nombre} no logra superar la defensa de {carta_defensora.nombre}. "
                          f"El jugador contrario pierde {dano} puntos de vida.")
                else:
                    print(f"{self.nombre} no puede superar la defensa de {carta_defensora.nombre}.")
        else:
            print(f"{self.nombre} no puede atacar porque está en modo defensa.")

        return puntos_vida_oponente

    def destruir(self, lista_cartas):
        if self in lista_cartas:
            lista_cartas.remove(self)
            print(f"{self.nombre} ha sido destruido y enviado al cementerio.")

    def cambiar_modo(self):
        self.en_ataque = False
        modal = "ataque" if self.en_ataque else "defensa"
        print(f"{self.nombre} ahora está en modo {modal}.")

    # Métodos adicionales
    def recibir_ataque_directo(self, puntos_vida_jugador, ataque):
        puntos_vida_jugador -= ataque
        print(f"{self.nombre} ataca de manera directa. El jugador pierde {ataque} puntos de vida.")
        return puntos_vida_jugador

    def __str__(self):
        modo = "Ataque" if self.en_ataque else "Defensa"
        return (f"{self.nombre} ({self.tipo_monstruo}/{self.elemento}) - "
                f"ATK: {self.ataque}, DEF: {self.defensa}, Modo: {modo}\n"
                f"Descripción: {self.descripcion}")