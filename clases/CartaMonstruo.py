from .Carta import Carta
from enums.elemento import Elemento
from enums.tipo_monstruo import TipoMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa

class CartaMonstruo(Carta):
    fusiones = {}  # Diccionario compartido para fusiones

    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo, elemento, modo):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo_monstruo = tipo_monstruo
        self.elemento = elemento
        self.en_ataque = modo

    # Métodos principales
    def atacar(self, carta_defensora, lista_cartas_trampa, puntos_vida_oponente):
        """
        Ataca a una carta defensora. Verifica cartas trampa y calcula daño según el modo de las cartas.
        """
        if not isinstance(carta_defensora, CartaMonstruo):
            print(f"{self.nombre} no puede atacar a {carta_defensora.nombre}, ya que no es un monstruo.")
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
                    carta_defensora.destruir()
                    puntos_vida_oponente -= (self.ataque - carta_defensora.ataque)
                elif self.ataque < carta_defensora.ataque:
                    print(f"{self.nombre} es destruido por {carta_defensora.nombre}.")
                    self.destruir()
                else:
                    print(f"El ataque termina en empate. Ningún monstruo es destruido.")
            else:
                # Ataque vs. Defensa
                if self.ataque > carta_defensora.defensa:
                    print(f"{self.nombre} destruye a {carta_defensora.nombre} en modo defensa.")
                    carta_defensora.destruir()
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
            self.estado = "cementerio"
            print(f"{self.nombre} ha sido destruida y enviada al cementerio.")
        else:
            print(f"{self.nombre} no está en el campo.")

    def cambiar_modo(self):
        self.en_ataque = not self.en_ataque
        modo = "ataque" if self.en_ataque else "defensa"
        print(f"{self.nombre} ahora está en modo {modo}.")

    # Métodos adicionales
    def recibir_ataque_directo(self, puntos_vida_jugador, ataque):
        puntos_vida_jugador -= ataque
        print(f"{self.nombre} no puede defender. El jugador pierde {ataque} puntos de vida.")
        return puntos_vida_jugador

    def fusionar_carta(self, carta_fusionada):
        for nombre_fusion, fusion in CartaMonstruo.fusiones.items():
            if self.nombre in fusion["cartas"] and carta_fusionada.nombre in fusion["cartas"]:
                print(f"¡Fusión exitosa! {self.nombre} y {carta_fusionada.nombre} forman {nombre_fusion}.")
                return CartaMonstruo(
                    nombre_fusion,
                    fusion["descripcion"],
                    self.ataque + carta_fusionada.ataque,
                    self.defensa + carta_fusionada.defensa,
                    self.tipo_monstruo,
                    self.elemento,
                    True,
                )
        print("Fusión fallida. Las cartas no cumplen los requisitos.")
        return None

    @staticmethod
    def cargar_fusiones(ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                nombre_fusion = datos[0]
                cartas_requeridas = datos[1:3]
                descripcion = datos[3]
                CartaMonstruo.fusiones[nombre_fusion] = {
                    "cartas": cartas_requeridas,
                    "descripcion": descripcion,
                }

    def __str__(self):
        modo = "Ataque" if self.en_ataque else "Defensa"
        return (f"{self.nombre} ({self.tipo_monstruo}/{self.elemento}) - "
                f"ATK: {self.ataque}, DEF: {self.defensa}, Modo: {modo}\n"
                f"Descripción: {self.descripcion}")