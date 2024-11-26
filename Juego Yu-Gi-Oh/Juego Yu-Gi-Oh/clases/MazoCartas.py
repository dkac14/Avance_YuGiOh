import random
from .CartaMonstruo import CartaMonstruo
from .CartaMagica import CartaMagica
from .CartaTrampa import CartaTrampa

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
                    mazo.append(CartaMonstruo(nombre,descripcion,int(ataque),int(defensa),monstruo,atributo))
            
                elif tipo_carta == "Magica":
                    nombre = datos[1]
                    descripcion = datos[2]
                    aumento_ataque = datos[3]
                    aumento_defensa = datos[4]
                    tipo_monstruo = datos[5]
                    mazo.append(CartaMagica(nombre,descripcion,int(aumento_ataque), int(aumento_defensa), tipo_monstruo))

                elif tipo_carta == "Trampa":
                    nombre = datos[1]
                    descripcion = datos[2]
                    atributo = datos[3]
                    mazo.append(CartaTrampa(nombre,descripcion,atributo))
        return mazo


    def seleccionar_mazo(self):

        cartas_cargadas = self.cargar_cartas()
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
