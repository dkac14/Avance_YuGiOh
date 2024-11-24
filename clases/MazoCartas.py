from clases.CartaMonstruo import CartaMonstruo
from clases.CartaMagica import CartaMagica
from clases.CartaTrampa import CartaTrampa
import random


class MazoCartas:
    def __init__(self):
        self.cartas = []

    @staticmethod
    def cargar_cartas(ruta_archivo):
        mazo = []
        with open(ruta_archivo, 'r') as archivo:

            for linea in archivo:
                datos = linea.strip().split(",")
                tipo_carta = datos[0]
            
                if tipo_carta == "Monstruo":
                    nombre = datos[1]
                    descripcion = datos[2]
                    ataque = datos[3]
                    defensa = datos[4]
                    atributo = datos[5]
                    monstruo = datos[6]
                    mazo.append(CartaMonstruo(nombre,descripcion,ataque,defensa,monstruo,atributo))
            
                elif tipo_carta == "Magica":
                    nombre = datos[1]
                    descripcion = datos[2]
                    aumento_ataque = datos[3]
                    aumento_defensa = datos[4]
                    tipo_monstruo = datos[5]
                    mazo.append(CartaMagica(nombre,descripcion,aumento_ataque, aumento_defensa, tipo_monstruo))

                elif tipo_carta == "Trampa":
                    nombre = datos[1]
                    descripcion = datos[2]
                    atributo = datos[3]
                    mazo.append(CartaTrampa(nombre,descripcion,atributo))
        return mazo



    def seleccionarMazo(self,archivo):
        print("x")
        c = self.cargar_cartas(archivo)
        print("x")

        random.shuffle(c)
        Cartas_monstruos = 0
        Cartas_magicas = 0
        Cartas_trampa = 0

        mazo = []
        for carta in c:
            if isinstance(carta, CartaMonstruo) and Cartas_monstruos <= 20:
                mazo.append(carta)
                Cartas_monstruos += 1
            elif isinstance(carta, CartaMagica) and Cartas_magicas <= 5:
                mazo.append(carta)
                Cartas_magicas += 1
            elif isinstance(carta, CartaTrampa) and Cartas_trampa <= 5:
                mazo.append(carta)
                Cartas_trampa += 1
        return mazo
