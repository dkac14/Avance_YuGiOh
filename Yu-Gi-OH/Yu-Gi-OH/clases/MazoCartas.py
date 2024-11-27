
import random


class MazoCartas:
    def __init__(self):
        self.cartas = []

    @staticmethod
    def cargar_cartas(ruta_archivo):
        from .CartaMonstruo import CartaMonstruo
        from .CartaMagica import CartaMagica
        from .CartaTrampa import CartaTrampa
        mazo = []
        with open(ruta_archivo, 'r',encoding='utf-8') as archivo:

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
                    mazo.append(CartaMonstruo(nombre,descripcion,int(ataque),int(defensa),atributo,monstruo,True))
            
                elif tipo_carta == "Magica":
                    nombre = datos[1]
                    descripcion = datos[2]
                    elemento = datos[3]
                    aumento = datos[4]
                    posicion = datos[5]
                    mazo.append(CartaMagica(nombre,descripcion,elemento,aumento,posicion))

                elif tipo_carta == "Trampa":
                    nombre = datos[1]
                    descripcion = datos[2]
                    atributo = datos[3]
                    mazo.append(CartaTrampa(nombre,descripcion,atributo))
        return mazo



    def seleccionarMazo(self,archivo):
        from .CartaMonstruo import CartaMonstruo
        from .CartaMagica import CartaMagica
        from .CartaTrampa import CartaTrampa
        c = self.cargar_cartas(archivo)
        
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

            if Cartas_monstruos == 20 and Cartas_magicas == 5 and Cartas_trampa == 5:
                break
        self.cartas = mazo
        return mazo
    

    def mostrar_mazo(self):
        for carta in self.cartas:
            print(carta)