from clases.Carta import Carta
from enums.elemento import Elemento
from enums.tipo_monstruo import TipoMonstruo


class CartaMonstruo(Carta):

    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo, elemento, modo):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo_monstruo = tipo_monstruo
        self.elemento = elemento
        self.en_ataque = modo
        self.fusiones = {}

    # Métodos getter y setter
    def get_ataque(self):
        return self.ataque

    def set_ataque(self, ataque):
        self.ataque = ataque

    def get_defensa(self):
        return self.defensa

    def set_defensa(self, defensa):
        self.defensa = defensa

    def get_tipo_monstruo(self):
        return self.tipo_monstruo

    def set_tipo_monstruo(self, tipo_monstruo):
        self.tipo_monstruo = tipo_monstruo

    def get_elemento(self):
        return self.elemento

    def set_elemento(self, elemento):
        self.elemento = elemento

    # Métodos principales
    def atacar(self, carta_defensora, lista_cartas):
        if not isinstance(carta_defensora, CartaMonstruo):
            print("No se puede atacar a esta carta, ya que no es un monstruo.")
            return

        if self.en_ataque:
            print(f"{self.nombre} está atacando a {carta_defensora.nombre}.")

            if carta_defensora.en_ataque:
                if self.ataque > carta_defensora.ataque:
                    print(f"{self.nombre} ha ganado el ataque. {carta_defensora.nombre} ha sido destruida.")
                    carta_defensora.destruir(lista_cartas)
                elif self.ataque < carta_defensora.ataque:
                    print(f"{self.nombre} ha perdido el ataque. {self.nombre} ha sido destruida.")
                    self.destruir(lista_cartas)
                else:
                    print(f"El ataque de {self.nombre} y {carta_defensora.nombre} es igual. Ninguna carta es destruida.")
            else:
                if self.ataque > carta_defensora.defensa:
                    print(f"{self.nombre} ha destruido a {carta_defensora.nombre}.")
                    carta_defensora.destruir(lista_cartas)
                elif self.ataque < carta_defensora.defensa:
                    print(f"{self.nombre} ha fallado el ataque. {carta_defensora.nombre} permanece en el campo.")
                else:
                    print(f"El ataque de {self.nombre} es igual a la defensa de {carta_defensora.nombre}. No ocurre nada.")
        else:
            print(f"{self.nombre} no puede atacar porque está en modo defensa.")

    def destruir(self, lista_cartas):
        if self in lista_cartas:
            lista_cartas.remove(self)
            print(f"{self.nombre} ha sido destruida y removida de la lista.")
        else:
            print(f"{self.nombre} no está en la lista de cartas.")

    @staticmethod
    def cargar_fusiones(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                nombre_fusion = datos[0]
                cartas_requeridas = datos[1:3]
                descripcion = datos[3]
                CartaMonstruo.fusiones[nombre_fusion] = {
                    "cartas": cartas_requeridas,
                    "descripcion": descripcion,
                }

    def cambiar_modo(self):
        self.en_ataque = not self.en_ataque
        modo = "ataque" if self.en_ataque else "defensa"
        print(f"{self.nombre} ahora está en modo de {modo}.")

    def fusionar_carta(self, carta_fusionada):
        for nombre_fusion, fusion in CartaMonstruo.fusiones.items():
            if self.nombre in fusion["cartas"] and carta_fusionada.nombre in fusion["cartas"]:
                print(f"¡Fusión exitosa! {self.nombre} y {carta_fusionada.nombre} se combinan para formar {nombre_fusion}.")
                return CartaMonstruo(
                    nombre_fusion,
                    fusion["descripcion"],
                    self.ataque + carta_fusionada.ataque,
                    self.defensa + carta_fusionada.defensa,
                    self.tipo_monstruo, 
                    self.elemento, 
                    True 
                )
        print("Fusión fallida: estas cartas no cumplen los requisitos.")
        return None

    def __str__(self):
        modo = "Ataque" if self.en_ataque else "Defensa"
        return (f"{self.nombre} ({self.tipo_monstruo}/{self.elemento}) - "
                f"ATK: {self.ataque}, DEF: {self.defensa}, Modo: {modo}\n"
                f"Descripción: {self.descripcion}")