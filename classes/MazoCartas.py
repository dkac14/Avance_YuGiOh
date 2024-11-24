from classes.CartaMonstruo import CartaMonstruo
from classes.CartaMagica import CartaMagica
from classes.CartaTrampa import CartaTrampa

import random


class MazoCartas:
    def __init__(self):
        self.cartas = []

    @staticmethod
    def cargar_cartas(ruta_archivo):
        """
        Carga cartas desde un archivo y las retorna en una lista.
        """
        mazo = []
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                tipo_carta = datos[0]

                if tipo_carta == "Monstruo":
                    nombre = datos[1]
                    descripcion = datos[2]
                    ataque = int(datos[3])
                    defensa = int(datos[4])
                    tipo_monstruo = datos[5]
                    elemento = datos[6]
                    mazo.append(
                        CartaMonstruo(
                            nombre=nombre,
                            descripcion=descripcion,
                            ataque=ataque,
                            defensa=defensa,
                            tipo_monstruo=tipo_monstruo,
                            elemento=elemento,
                            modo=True,
                        )
                    )

                elif tipo_carta == "Magica":
                    nombre = datos[1]
                    descripcion = datos[2]
                    tipo_monstruo = datos[3]
                    incremento = int(datos[4])
                    tipo_incremento = datos[5]
                    mazo.append(
                        CartaMagica(
                            nombre=nombre,
                            descripcion=descripcion,
                            tipo_monstruo=tipo_monstruo,
                            incremento=incremento,
                            tipo_incremento=tipo_incremento,
                        )
                    )

                elif tipo_carta == "Trampa":
                    nombre = datos[1]
                    descripcion = datos[2]
                    tipo_atributo = datos[3]
                    mazo.append(
                        CartaTrampa(
                            nombre=nombre,
                            descripcion=descripcion,
                            tipo_atributo=tipo_atributo,
                        )
                    )
        return mazo

    def seleccionar_mazo(self, ruta_archivo):

        cartas_cargadas = self.cargar_cartas(ruta_archivo)
        random.shuffle(cartas_cargadas)

        mazo = []
        conteo_monstruos = 0
        conteo_magicas = 0
        conteo_trampas = 0

        for carta in cartas_cargadas:
            if isinstance(carta, CartaMonstruo) and conteo_monstruos < 20:
                mazo.append(carta)
                conteo_monstruos += 1
            elif isinstance(carta, CartaMagica) and conteo_magicas < 5:
                mazo.append(carta)
                conteo_magicas += 1
            elif isinstance(carta, CartaTrampa) and conteo_trampas < 5:
                mazo.append(carta)
                conteo_trampas += 1

            if conteo_monstruos == 20 and conteo_magicas == 5 and conteo_trampas == 5:
                break

        self.cartas = mazo
        return mazo

    def mostrar_mazo(self):
        for carta in self.cartas:
            print(carta)

