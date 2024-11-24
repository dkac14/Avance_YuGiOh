from .carta import Carta
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

    @staticmethod
    def cargar_fusiones(ruta_archivo):
        """Carga las fusiones desde un archivo .txt."""
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                nombre_fusion = datos[0]
                cartas_requeridas = datos[1:3]  # Las dos cartas necesarias para la fusión
                descripcion = datos[3]
                CartaMonstruo.fusiones[nombre_fusion] = {
                    "cartas": cartas_requeridas,
                    "descripcion": descripcion,
                }

    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo, elemento, en_ataque):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.tipo_monstruo = tipo_monstruo
        self.elemento = elemento
        self.en_ataque = en_ataque.lower() == "true"
        self.cartas = {}

    def __str__(self):
        modo = "Ataque" if self.en_ataque else "Defensa"
        return (f"{self.nombre} ({self.tipo_monstruo}/{self.elemento}) - "
                f"ATK: {self.ataque}, DEF: {self.defensa}, Modo: {modo}\n"
                f"Descripción: {self.descripcion}")

    def fusionar_carta(self, carta_fusionada):
        for nombre_fusion, fusion in CartaMonstruo.fusiones.items():
            if self.nombre in fusion["cartas"] and carta_fusionada.nombre in fusion["cartas"]:
                print(f"¡Fusión exitosa! {self.nombre} y {carta_fusionada.nombre} se combinan para formar {nombre_fusion}.")
                return CartaMonstruo(
                    nombre_fusion,
                    fusion["descripcion"],
                    self.ataque + carta_fusionada.ataque,  # Combina los atributos
                    self.defensa + carta_fusionada.defensa,
                    self.tipo_monstruo,  # Mantiene el tipo del primer monstruo
                    self.elemento,  # Mantiene el elemento del primer monstruo
                    True  # La carta fusionada empieza en modo ataque
                )
        print("Fusión fallida: estas cartas no cumplen los requisitos.")
        return None

    def cambiar_modo(self):
        """Cambia el modo de la carta (ataque o defensa)."""
        self.en_ataque = not self.en_ataque
        modo = "ataque" if self.en_ataque else "defensa"
        print(f"{self.nombre} ahora está en modo de {modo}.")

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

