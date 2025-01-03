import random
import numpy as np

class Carta:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, tipo_monstruo, incremento, tipo_incremento):
        super().__init__(nombre, descripcion)
        self.tipo_monstruo = tipo_monstruo
        self.incremento = incremento
        self.tipo_incremento = tipo_incremento
        self.equipada_a = None

    def activar_carta(self, monstruo):
        if monstruo.tipo_monstruo == self.tipo_monstruo:
            self.equipada_a = monstruo
            if self.tipo_incremento == "ataque":
                monstruo.ataque += self.incremento
                print(f"{self.nombre} equipada a {monstruo.nombre}. Incrementa su {self.tipo_incremento} en {self.incremento}.")
                return monstruo.ataque  # Retorna los puntos de ataque totales tras el bufo.
            elif self.tipo_incremento == "defensa":
                monstruo.defensa += self.incremento
                print(f"{self.nombre} equipada a {monstruo.nombre}. Incrementa su {self.tipo_incremento} en {self.incremento}.")
                return monstruo.defensa  # Retorna los puntos de defensa totales tras el bufo.
        else:
            print(f"{self.nombre} no puede equiparse a {monstruo.nombre} porque no es del tipo {self.tipo_monstruo}.")
            return None

    def destruir(self, lista_cartas, lista_monstruos):
        if self.equipada_a:
            if self.equipada_a not in lista_monstruos:
                print(f"{self.nombre} ha sido destruida porque {self.equipada_a.nombre} ya no está en el campo.")
                lista_cartas.remove(self)
                self.equipada_a = None
                
    def __str__(self):
        return (f"{self.nombre}")



class CartaMonstruo(Carta):

    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo, elemento, modo):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo_monstruo = tipo_monstruo
        self.elemento = elemento
        self.en_ataque = modo

    # Métodos principales
    def atacar(self, carta_enemigo, puntos_vida_oponente, puntos_vida_atacante, eleccion_atacantes, eleccion_defensor, tablero_atk, tablero_def):
        """
        Ataca a una carta defensora. Verifica cartas trampa y calcula daño según el modo de las cartas.
        """
        # Ataque directo
        if carta_enemigo is None:
            puntos_vida_oponente -= self.ataque
            print(f"Ataque directo: {self.nombre} inflige {self.ataque} puntos de daño.")
            return puntos_vida_oponente

        # Verifica si la carta enemiga es válida
        elif not isinstance(carta_enemigo, CartaMonstruo):
            print(f"{self.nombre} no puede atacar a la carta, ya que no es un monstruo.")
            return puntos_vida_oponente

        print(f"{self.nombre} declara un ataque a {carta_enemigo.nombre}.")

        # Verificar cartas trampa
        for i, carta_trampa in enumerate(tablero_def.obtener_cartas_trampa()):
            if isinstance(carta_trampa, CartaTrampa) and carta_trampa.verificar(self):
                carta_trampa.activar(self, tablero_def.obtener_cartas_trampa(), tablero_def, i)
                return puntos_vida_oponente

        # Continuar con el ataque si no hay trampas activadas
        if self.en_ataque:
            if carta_enemigo.en_ataque:
                # Ataque vs. Ataque
                if self.ataque > carta_enemigo.ataque:
                    print(f"{self.nombre} destruye a {carta_enemigo.nombre}.")
                    carta_enemigo.destruir(tablero_def.obtener_cartas_monstruo())
                    tablero_def.eliminar_carta_monstruo(eleccion_defensor)
                    puntos_vida_oponente -= (self.ataque - carta_enemigo.ataque)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(tablero_def.obtener_cartas_magicas()):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == carta_enemigo:
                            carta_magica.destruir(tablero_def.obtener_cartas_magicas(), tablero_def.obtener_cartas_monstruo())
                            tablero_def.eliminar_carta_magica_trampa(i)

                elif self.ataque < carta_enemigo.ataque:
                    print(f"{self.nombre} es destruido por {carta_enemigo.nombre}.")
                    self.destruir(tablero_atk.obtener_cartas_monstruo())
                    tablero_atk.eliminar_carta_monstruo(eleccion_atacantes)
                    puntos_vida_atacante -= (carta_enemigo.ataque - self.ataque)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(tablero_atk.obtener_cartas_magicas()):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == self:
                            carta_magica.destruir(tablero_atk.obtener_cartas_magicas(), tablero_atk.obtener_cartas_monstruo())
                            tablero_atk.eliminar_carta_magica_trampa(i)
                    
                    return puntos_vida_atacante

                else:
                    print(f"El ataque termina en empate. Los 2 monstruos son destruidos.")
                    print(f"{self.nombre} destruye a {carta_enemigo.nombre}.")
                    carta_enemigo.destruir(tablero_def.obtener_cartas_monstruo())
                    tablero_def.eliminar_carta_monstruo(eleccion_defensor)
                    puntos_vida_oponente -= (self.ataque - carta_enemigo.ataque)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(tablero_def.obtener_cartas_magicas()):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == carta_enemigo:
                            carta_magica.destruir(tablero_def.obtener_cartas_magicas(), tablero_def.obtener_cartas_monstruo())
                            tablero_def.eliminar_carta_magica_trampa(i)

                    print(f"{self.nombre} es destruido por {carta_enemigo.nombre}.")
                    self.destruir(tablero_atk.obtener_cartas_monstruo())
                    tablero_atk.eliminar_carta_monstruo(eleccion_atacantes)
                    puntos_vida_atacante -= (carta_enemigo.ataque - self.ataque)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(tablero_atk.obtener_cartas_magicas()):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == self:
                            carta_magica.destruir(tablero_atk.obtener_cartas_magicas(), tablero_atk.obtener_cartas_monstruo())
                            tablero_atk.eliminar_carta_magica_trampa(i)

            else:
                # Ataque vs. Defensa
                if self.ataque > carta_enemigo.defensa:
                    print(f"{self.nombre} destruye a {carta_enemigo.nombre} en modo defensa.")
                    carta_enemigo.destruir(tablero_def.obtener_cartas_monstruo())
                    tablero_def.eliminar_carta_monstruo(eleccion_defensor)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(tablero_def.obtener_cartas_magicas()):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == carta_enemigo:
                            carta_magica.destruir(tablero_def.obtener_cartas_magicas(), tablero_def.obtener_cartas_monstruo())
                            tablero_def.eliminar_carta_magica_trampa(i)

                elif self.ataque < carta_enemigo.defensa:
                    dano = carta_enemigo.defensa - self.ataque
                    puntos_vida_atacante -= dano
                    print(f"{self.nombre} no logra superar la defensa de {carta_enemigo.nombre}. "
                        f"El jugador pierde {dano} puntos de vida.")
                    return puntos_vida_atacante

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
    def recibir_ataque_directo(self, puntos_vida_jugador, ataque, tablero_def):
        
        for i, carta_trampa in enumerate(tablero_def.obtener_cartas_trampa()):
            if isinstance(carta_trampa, CartaTrampa) and carta_trampa.verificar(self):
                carta_trampa.activar(self, tablero_def.obtener_cartas_trampa(), tablero_def, i)
                return None
            
        puntos_vida_jugador -= ataque
        print(f"{self.nombre} ataca de manera directa. El jugador pierde {ataque} puntos de vida.")
        return puntos_vida_jugador

    def __str__(self):
        modo = "Ataque" if self.en_ataque else "Defensa"
        return (f"{self.nombre} ({self.tipo_monstruo}/{self.elemento}) - "
                f"ATK: {self.ataque}, DEF: {self.defensa}")
    
class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, tipo_atributo):
        super().__init__(nombre, descripcion)
        self.tipo_atributo = tipo_atributo
        self.boca_abajo = True 

    def verificar(self, carta_atacante):
        verificacion = carta_atacante.elemento == self.tipo_atributo
        return verificacion

    def activar(self, carta_atacante, lista_cartas, tablero, indice):

        if isinstance(carta_atacante, CartaMonstruo) and carta_atacante.elemento == self.tipo_atributo:
            print(f"{self.nombre} ha sido activada y detiene el ataque de {carta_atacante.nombre}.")
            self.boca_abajo = False
            self.descartar(lista_cartas)
            tablero.eliminar_carta_magica_trampa(indice)
        else:
            print(f"{self.nombre} no puede activarse porque {carta_atacante.nombre} no tiene el atributo {self.tipo_atributo}.")

    def descartar(self, lista_cartas):
        if self in lista_cartas:
            lista_cartas.remove(self)
            print(f"{self.nombre} ha sido descartada después de ser utilizada.")

    def __str__(self):
        return "Carta Trampa"

from enum import Enum

class Elemento(Enum):
    OSCURIDAD = "Oscuridad"
    LUZ = "Luz"
    TIERRA = "Tierra"
    AGUA = "Agua"
    FUEGO = "Fuego"
    VIENTO = "Viento"

class Jugador:
    def __init__(self, nombre, mazo):
        self.nombre = nombre
        self.vida = 4000
        self.mazo = mazo
        self.mano = self.inicializar_mano()
        self.tablero = Tablero()

    def inicializar_mano(self):
        mano_inicial = []
        for _ in range(4):
            if self.mazo:
                mano_inicial.append(self.mazo.pop(0))
        return mano_inicial
    
    def robar_carta(self):
        if self.mazo:
            carta = self.mazo.pop(0)
            self.mano.append(carta)
            print(f"{self.nombre} robó la carta: {carta.nombre}")
        else:
            print(f"{self.nombre} no tiene más cartas en el mazo.")

    def jugar_carta(self):
        if not self.mano:
            print("No tienes cartas en tu mano para jugar.")
            return

        print("Cartas en tu mano:")
        for i, carta in enumerate(self.mano):
            if isinstance(carta, CartaMonstruo): 
                print(f"{i + 1}. {carta.nombre} ({type(carta).__name__}) - {carta.descripcion} (Ataque:{carta.ataque} Defensa:{carta.defensa})")
            else:
                print(f"{i + 1}. {carta.nombre} ({type(carta).__name__}) - {carta.descripcion}")

        eleccion = -1
        while eleccion < 0 or eleccion >= len(self.mano):
            entrada = input("Selecciona el número de la carta que deseas jugar: ")
            if entrada.isdigit():
                eleccion = int(entrada) - 1
            else:
                print("Entrada no válida. Por favor, introduce un número.")

        carta = self.mano[eleccion]

        if isinstance(carta, CartaMonstruo):
            modo = input("¿En qué modo quieres jugar la carta? (ataque/defensa): ").strip().lower()
            while modo not in ["ataque", "defensa"]:
                modo = input("¿En qué modo quieres jugar la carta? (ataque/defensa): ").strip().lower()
                if modo not in ["ataque", "defensa"]:
                    print("Opción inválida. Por favor, ingresa 'ataque' o 'defensa'.")
            if modo == "defensa":
                carta.cambiar_modo()

            if self.tablero.agregar_carta_monstruo(carta):
                print(f"Jugaste {carta.nombre} en modo {'ataque' if carta.en_ataque else 'defensa'}.")
        
        elif isinstance(carta, CartaMagica):
            if not self.tablero.obtener_cartas_monstruo():
                print("No hay monstruos en el campo para aplicar esta carta mágica.")
                return

            encontro = 0
            # Recorre las cartas monstruo en el tablero.
            for monstruo in self.tablero.obtener_cartas_monstruo():
                # Verifica si el tipo de monstruo coincide con el tipo de la carta mágica.
                if monstruo.tipo_monstruo == carta.tipo_monstruo:
                    # Activa la carta mágica en el monstruo y actualiza el atributo correspondiente.
                    if carta.tipo_incremento == "ataque":
                        carta.ataque = carta.activar_carta(monstruo)  # Actualiza el ataque del monstruo.
                    elif carta.tipo_incremento == "defensa":
                        carta.defensa = carta.activar_carta(monstruo)  # Actualiza la defensa del monstruo.

                    # Agrega la carta mágica al tablero tras la activación.
                    self.tablero.agregar_carta_magica_o_trampa(carta)
                    encontro = 1
                    print(f"{monstruo.nombre} equipado con {carta.nombre}.")

            # Si no se encontró un monstruo compatible.
            if encontro == 0:
                print("No hay monstruos de este tipo en el campo para aplicar esta carta mágica.")
                
            
        elif isinstance(carta, CartaTrampa):
            self.tablero.agregar_carta_magica_o_trampa(carta)  
            print(f"Jugaste la carta trampa: {carta.nombre} (boca abajo).")

        self.mano.remove(carta)

    def declarar_batalla(self, gamer):

        if self.tablero.turno < 2:
            print("No puedes declarar batalla hasta el segundo turno.")
            self.tablero.turno += 1
            return

        monstruos_atacantes = self.tablero.obtener_cartas_monstruo()
        monstruos_defensores = gamer.tablero.obtener_cartas_monstruo()

        if not monstruos_atacantes:
            print("No tienes monstruos en tu campo para declarar una batalla.")
            return

        monstruos_ya_usados = set()

        while len(monstruos_atacantes) > len(monstruos_ya_usados):
            print("\nMonstruos disponibles para atacar:")
            for i, monstruo in enumerate(monstruos_atacantes):
                if monstruo not in monstruos_ya_usados:
                    print(f"{i + 1}. {monstruo}")

            eleccion_atacante = int(input("Selecciona el número del monstruo atacante (o 0 para salir): ")) - 1
            if eleccion_atacante == -1:
                print("Terminaste la fase de batalla.")
                break

            if eleccion_atacante < 0 or eleccion_atacante >= len(monstruos_atacantes):
                print("Selección inválida. Intenta nuevamente.")
                continue

            carta_atacante = monstruos_atacantes[eleccion_atacante]
            if carta_atacante in monstruos_ya_usados:
                print(f"{carta_atacante.nombre} ya atacó este turno.")
                continue

            print("\nOpciones de ataque:")
            print("1. Ataque directo al jugador.")
            print("2. Ataque a un monstruo defensor.")
            tipo_ataque = input("Elige el tipo de ataque: ").strip()

            if tipo_ataque == "1":  # Ataque directo
                if len(monstruos_defensores) > 0:
                    print("El oponente tiene monstruos en el campo.")
                    continue
                else:
                    print(f"{carta_atacante.nombre} realiza un ataque directo.")
                    gamer.vida = carta_atacante.recibir_ataque_directo(gamer.vida, carta_atacante.ataque, gamer.tablero)

            elif tipo_ataque == "2":  # Ataque a un monstruo defensor
                if not monstruos_defensores:
                    print("El oponente no tiene monstruos en el campo. Realiza un ataque directo.")
                    continue

                print("Monstruos defensores disponibles:")
                for i, defensor in enumerate(monstruos_defensores):
                    print(f"{i + 1}. {defensor}")

                eleccion_defensor = int(input("Selecciona el número del monstruo defensor: ")) - 1
                if eleccion_defensor < 0 or eleccion_defensor >= len(monstruos_defensores):
                    print("Selección inválida. Intenta nuevamente.")
                    continue

                carta_defensora = monstruos_defensores[eleccion_defensor]
                gamer.vida = carta_atacante.atacar(carta_defensora, gamer.vida, self.vida, eleccion_atacante, eleccion_defensor, self.tablero, gamer.tablero)

            else:
                print("Opción inválida. Intenta nuevamente.")
                continue

            monstruos_ya_usados.add(carta_atacante)
            continuar = input("¿Deseas continuar atacando? (si/no): ").strip().lower()
            while continuar != "si" and continuar != "no":
                print("Respuesta inválida. Por favor, responde con 'si' o 'no'.")
                continuar = input("¿Deseas continuar atacando? (si/no): ").strip().lower()

            if continuar == "no":
                print("Terminaste la fase de batalla.")
                break


class JugadorMaquina:
    def __init__(self, nombre, mazo):
        self.nombre = nombre
        self.vida = 4000
        self.mazo = mazo
        self.mano = self.inicializar_mano()
        self.tablero = Tablero()

    def inicializar_mano(self):
        mano_inicial = []
        for _ in range(4):
            if self.mazo:
                mano_inicial.append(self.mazo.pop(0))
        return mano_inicial

    def robar_carta(self):
        if self.mazo:
            carta = self.mazo.pop(0)
            self.mano.append(carta)
            print(f"{self.nombre} robó la carta: {carta.nombre}")
        else:
            print(f"{self.nombre} no tiene más cartas en el mazo.")

    def jugar_carta(self):
        if not self.mano:
            print(f"{self.nombre} no tiene cartas en su mano para jugar.")
            return

        carta = random.choice(self.mano)

        if isinstance(carta, CartaMonstruo):
            modo = random.choice(["ataque", "defensa"])
            if modo == "defensa":
                carta.cambiar_modo()

            if self.tablero.agregar_carta_monstruo(carta):
                print(f"{self.nombre} jugó {carta.nombre} en modo {'ataque' if carta.en_ataque else 'defensa'}.")

        elif isinstance(carta, CartaMagica):
            if not self.tablero.obtener_cartas_monstruo():
                print("No hay monstruos en el campo para aplicar esta carta mágica.")
                return

            encontro = 0
            # Recorre las cartas monstruo en el tablero.
            for monstruo in self.tablero.obtener_cartas_monstruo():
                # Verifica si el tipo de monstruo coincide con el tipo de la carta mágica.
                if monstruo.tipo_monstruo == carta.tipo_monstruo:
                    # Activa la carta mágica en el monstruo y actualiza el atributo correspondiente.
                    if carta.tipo_incremento == "ataque":
                        carta.ataque = carta.activar_carta(monstruo)  # Actualiza el ataque del monstruo.
                    elif carta.tipo_incremento == "defensa":
                        carta.defensa = carta.activar_carta(monstruo)  # Actualiza la defensa del monstruo.

                    # Agrega la carta mágica al tablero tras la activación.
                    self.tablero.agregar_carta_magica_o_trampa(carta)
                    encontro = 1
                    print(f"{monstruo.nombre} equipado con {carta.nombre}.")

            # Si no se encontró un monstruo compatible.
            if encontro == 0:
                print("No hay monstruos de este tipo en el campo para aplicar esta carta mágica.")
            
        elif isinstance(carta, CartaTrampa):
            self.tablero.agregar_carta_magica_o_trampa(carta)
            print(f"{self.nombre} jugó la carta trampa {carta.nombre} (boca abajo).")

        self.mano.remove(carta)

    def declarar_batalla(self, gamer):
        if self.tablero.turno < 2:
            print(f"{self.nombre} no puede declarar batalla hasta el segundo turno.")
            self.tablero.turno += 1
            return

        monstruos_atacantes = self.tablero.obtener_cartas_monstruo()
        monstruos_defensores = gamer.tablero.obtener_cartas_monstruo()

        if not monstruos_atacantes:
            print(f"{self.nombre} no tiene monstruos en su campo para declarar una batalla.")
            return

        monstruos_ya_usados = set()

        while len(monstruos_atacantes) > len(monstruos_ya_usados):
            # Seleccionar monstruo atacante aleatoriamente que no haya atacado aún
            carta_atacante = random.choice([m for m in monstruos_atacantes if m not in monstruos_ya_usados])

            # Decidir tipo de ataque: directo (1) o a un defensor (2)
            if monstruos_defensores and random.choice([1, 2]) == 2:  # Ataque a defensor
                carta_defensora = random.choice(monstruos_defensores)
                gamer.vida = carta_atacante.atacar(
                    carta_defensora,
                    gamer.vida,
                    self.vida,
                    monstruos_atacantes.index(carta_atacante),
                    monstruos_defensores.index(carta_defensora),
                    self.tablero,
                    gamer.tablero,
                )
                print(f"{self.nombre} atacó a {carta_defensora.nombre} con {carta_atacante.nombre}.")
            else:  # Ataque directo
                if monstruos_defensores:
                    print(f"{self.nombre} no puede realizar un ataque directo porque hay monstruos defensores.")
                else:
                    gamer.vida = carta_atacante.recibir_ataque_directo(gamer.vida, carta_atacante.ataque, gamer.tablero)
                    print(f"{self.nombre} realizó un ataque directo con {carta_atacante.nombre}.")

            # Marcar el monstruo como usado
            monstruos_ya_usados.add(carta_atacante)

            # Si todos los monstruos han atacado, termina la fase
            if len(monstruos_ya_usados) == len(monstruos_atacantes):
                print(f"{self.nombre} ha terminado la fase de batalla.")
                break

class MazoCartas:
    def __init__(self):
        self.cartas = []

    @staticmethod
    def cargar_cartas():
        """
        Carga cartas desde un archivo y las retorna en una lista.
        """
        mazo = []
        mounstruo = [
            ["Dragón de Ojos Rojos", "Un dragón con ojos rojos que tiene gran poder de ataque.", 2400, 2000, "FUEGO", "D", True],
            ["Guerrero Legendario", "Un guerrero con una espada mágica que defiende el reino.", 1800, 1500, "TIERRA", "G", False],
            ["Zombi Nocturno", "Un zombi que se mueve solo de noche, con gran resistencia.", 1200, 1000, "OSCURIDAD", "Z", True],
            ["Bestia de la Jungla", "Una feroz bestia que se oculta en la jungla esperando su presa.", 1600, 1200, "VIENTO", "B", False],
            ["Demonio Infernal", "Un demonio que surge del infierno con poder destructivo.", 2200, 1800, "OSCURIDAD", "O", True],
            ["Dragón de Fuego", "Un dragón con llamas abrasadoras, su poder de ataque es imparable.", 2100, 1900, "FUEGO", "D", True],
            ["Guerrero de Tierra", "Un guerrero de la tierra que se defiende con su escudo, gran resistencia.", 1700, 2100, "TIERRA", "G", False],
            ["Zombi de la Tumba", "Un zombi que revive desde las tumbas, y está dispuesto a atacar.", 1300, 1000, "OSCURIDAD", "Z", True],
            ["León Bestia", "Un león con gran agilidad que se mueve rápidamente en la jungla.", 1500, 1300, "VIENTO", "B", False],
            ["Diablo Nocturno", "Un demonio de las sombras, con un ataque devastador.", 2300, 1600, "OSCURIDAD", "O", True],
            ["Dragón del Trueno", "Un dragón que lanza rayos de gran poder, muy difícil de derrotar.", 2500, 2300, "FUEGO", "D", True],
            ["Guerrero de Acero", "Un guerrero con armadura de acero, casi imbatible.", 1900, 2500, "TIERRA", "G", False],
            ["Zombi Asesino", "Un zombi muy agresivo, dispuesto a atacar sin piedad.", 1400, 1200, "OSCURIDAD", "Z", True],
            ["Pantera Bestia", "Una pantera de gran agilidad y ferocidad, difícil de atrapar.", 1800, 1400, "VIENTO", "B", False],
            ["Ángel Demoníaco", "Un ángel caído con poderes demoníacos que causa estragos.", 2500, 2000, "OSCURIDAD", "O", True],
            ["Dragón Oscuro", "Un dragón con escamas oscuras que causa terror en el campo.", 2700, 2400, "FUEGO", "D", True],
            ["Guerrero Bestia", "Un guerrero que monta una bestia, luchan juntos en batalla.", 1600, 1600, "TIERRA", "G", False],
            ["Zombi Reanimado", "Un zombi resucitado por oscuros rituales, extremadamente resistente.", 1500, 1800, "OSCURIDAD", "Z", False],
            ["Bestia Mística", "Una bestia de gran agilidad que ataca con ferocidad.", 1700, 1400, "VIENTO", "B", False],
            ["Demonio Infernal", "Un demonio del abismo con un poder maligno enorme.", 2400, 2200, "OSCURIDAD", "O", True],
            ["Dragón de Hielo", "Un dragón con poderes de hielo que congela a sus enemigos.", 2200, 2000, "FUEGO", "D", True],
            ["Guerrero de Fuego", "Un guerrero con una espada ardiente, capaz de quemar a sus enemigos.", 1900, 1500, "TIERRA", "G", False],
            ["Zombi Destructor", "Un zombi de gran tamaño con poder de ataque superior.", 1600, 1300, "OSCURIDAD", "Z", True],
            ["León de la Selva", "Un león que caza en la selva con velocidad y precisión.", 1700, 1400, "VIENTO", "B", False],
            ["Rey Demonio", "Un rey demoníaco con gran poder y liderazgo en el inframundo.", 2500, 2200, "OSCURIDAD", "O", True],
            ["Dragón Fluvial", "Un dragón acuático que ataca desde las profundidades del mar.", 2300, 2100, "FUEGO", "D", True],
            ["Guerrero de la Luz", "Un guerrero con una espada brillante que lucha por la justicia.", 1900, 1700, "TIERRA", "G", False],
            ["Zombi Esquelético", "Un zombi que ha sido despojado de su carne, pero sigue en pie.", 1400, 1000, "OSCURIDAD", "Z", True],
            ["Leopardo Bestia", "Un leopardo con un agudo instinto de caza.", 1600, 1300, "VIENTO", "B", False],
            ["Diablo Siniestro", "Un demonio con un poder de ataque muy alto y malvado.", 2500, 2000, "OSCURIDAD", "O", True],
            ["Dragón Torbellino", "Un dragón que genera vientos huracanados con su poderoso vuelo.", 2400, 2300, "FUEGO", "D", True],
            ["Guerrero Acorazado", "Un guerrero con una armadura pesada, resistente a los ataques.", 2000, 2500, "TIERRA", "G", False],
            ["Zombi Fatal", "Un zombi extremadamente rápido y peligroso para sus oponentes.", 1600, 1400, "OSCURIDAD", "Z", True],
            ["Bestia Carnívora", "Una bestia feroz que devora todo a su paso.", 1800, 1600, "VIENTO", "B", False],
            ["Ángel Caído", "Un ángel que cayó del cielo, ahora sirve al mal.", 2500, 2100, "OSCURIDAD", "O", True],
            ["Dragón de Lava", "Un dragón que lanza lava hirviente con un gran poder destructivo.", 2200, 2000, "FUEGO", "D", True],
            ["Guerrero del Bosque", "Un guerrero que protege el bosque, con fuerza natural.", 1600, 1700, "TIERRA", "G", False],
            ["Zombi Aterrador", "Un zombi con una apariencia espantosa, que causa miedo a todos.", 1300, 1200, "OSCURIDAD", "Z", True],
            ["Bestia Rápida", "Una bestia de gran velocidad que sorprende a sus enemigos.", 1700, 1500, "VIENTO", "B", False],
            ["Demonio Maléfico", "Un demonio que siembra caos y destrucción en su camino.", 2400, 2100, "OSCURIDAD", "O", True],
            ["Dragón Tempestad", "Un dragón que controla el viento y la tormenta.", 2300, 2100, "FUEGO", "D", True],
            ["Guerrero Subterráneo", "Un guerrero que usa la tierra como su aliado, siempre camuflándose.", 1900, 2100, "TIERRA", "G", False],
            ["Zombi Fantasmal", "Un zombi cuya presencia es tan aterradora que paraliza a sus enemigos.", 1500, 1300, "OSCURIDAD", "Z", True],
            ["León Viento", "Un león que controla los vientos a su alrededor para moverse rápidamente.", 1800, 1500, "VIENTO", "B", False],
            ["Reina Demoníaca", "Una demoníaca reina que tiene un gran poder sobre sus súbditos.", 2400, 2000, "OSCURIDAD", "O", True],
            ["Dragón del Volcán", "Un dragón con la capacidad de liberar fuego volcánico a voluntad.", 2500, 2200, "FUEGO", "D", True],
            ["Guerrero de Hielo", "Un guerrero que usa la magia del hielo para protegerse.", 2000, 2300, "TIERRA", "G", False],
            ["Zombi Esquelético", "Un zombi con un esqueleto resquebrajado pero con gran resistencia.", 1500, 1200, "OSCURIDAD", "Z", True],
            ["León Montaña", "Un león que vive en las montañas, con gran fuerza física.", 1900, 1800, "VIENTO", "B", False],
            ["Dragón Viento", "Un dragón que puede controlar el viento y lanzar tornados.", 2200, 2000, "FUEGO", "D", True]
        ]

        magicas = [
            ["Espada de Arturo", "Incrementa en 200 el ataque de monstruos de tipo Guerrero.", "G", 200, "ataque"],
            ["Escudo de Chamelote", "Incrementa en 200 la defensa de monstruos de tipo Guerrero.", "G", 200, "defensa"],
            ["Capa Mística", "Incrementa en 150 el ataque de monstruos de tipo Dragón.", "D", 150, "ataque"],
            ["Amuletos de Fuego", "Incrementa en 100 la defensa de monstruos de tipo Dragón.", "D", 100, "defensa"],
            ["Anillo Zombi", "Incrementa en 100 el ataque de monstruos de tipo Zombi.", "Z", 100, "ataque"],
            ["Escudo Oscuro", "Incrementa en 150 la defensa de monstruos de tipo Zombi.", "Z", 150, "defensa"],
            ["Espada del Viento", "Incrementa en 250 el ataque de monstruos de tipo Bestia.", "B", 250, "ataque"],
            ["Escudo del Viento", "Incrementa en 150 la defensa de monstruos de tipo Bestia.", "B", 150, "defensa"],
            ["Poder del Guerrero", "Incrementa en 300 el ataque de monstruos de tipo Guerrero.", "G", 300, "ataque"],
            ["Coraza de Hierro", "Incrementa en 250 la defensa de monstruos de tipo Guerrero.", "G", 250, "defensa"],
            ["Báculo del Lanzador", "Incrementa en 200 el ataque de monstruos de tipo Lanzador de Conjuros.", "L", 200, "ataque"],
            ["Escudo Protector", "Incrementa en 150 la defensa de monstruos de tipo Lanzador de Conjuros.", "L", 150, "defensa"],
            ["Anillo del Demonio", "Incrementa en 250 el ataque de monstruos de tipo Demonio.", "O", 250, "ataque"],
            ["Amparo Demoníaco", "Incrementa en 200 la defensa de monstruos de tipo Demonio.", "O", 200, "defensa"],
            ["Luz Sagrada", "Incrementa en 150 el ataque de monstruos de tipo Lanzador de Conjuros.", "L", 150, "ataque"],
            ["Fuego Infernal", "Incrementa en 100 la defensa de monstruos de tipo Dragón.", "D", 100, "defensa"],
            ["Garras del Guerrero", "Incrementa en 180 el ataque de monstruos de tipo Guerrero.", "G", 180, "ataque"],
            ["Espada del Dragón", "Incrementa en 250 el ataque de monstruos de tipo Dragón.", "D", 250, "ataque"],
            ["Escudo de la Bestia", "Incrementa en 200 la defensa de monstruos de tipo Bestia.", "B", 200, "defensa"],
            ["Amuleto Zombi", "Incrementa en 150 el ataque de monstruos de tipo Zombi.", "Z", 150, "ataque"],
            ["Fuerza Demoníaca", "Incrementa en 200 el ataque de monstruos de tipo Demonio.", "O", 200, "ataque"],
            ["Llama de Fuego", "Incrementa en 100 la defensa de monstruos de tipo Dragón.", "D", 100, "defensa"],
            ["Corazón del Guerrero", "Incrementa en 250 la defensa de monstruos de tipo Guerrero.", "G", 250, "defensa"],
            ["Flecha del Viento", "Incrementa en 200 el ataque de monstruos de tipo Bestia.", "B", 200, "ataque"],
            ["Escudo de los Muertos", "Incrementa en 200 la defensa de monstruos de tipo Zombi.", "Z", 200, "defensa"],
            ["Espada del Guerrero", "Incrementa en 180 el ataque de monstruos de tipo Guerrero.", "G", 180, "ataque"],
            ["Escudo de Fuego", "Incrementa en 150 la defensa de monstruos de tipo Dragón.", "D", 150, "defensa"],
            ["Poder del Zombi", "Incrementa en 120 el ataque de monstruos de tipo Zombi.", "Z", 120, "ataque"],
            ["Luz del Guerrero", "Incrementa en 200 la defensa de monstruos de tipo Guerrero.", "G", 200, "defensa"],
            ["Escudo Viento", "Incrementa en 180 la defensa de monstruos de tipo Bestia.", "B", 180, "defensa"],
            ["Espada de los Muertos", "Incrementa en 250 el ataque de monstruos de tipo Zombi.", "Z", 250, "ataque"],
            ["Escudo de Dragón", "Incrementa en 200 la defensa de monstruos de tipo Dragón.", "D", 200, "defensa"],
            ["Báculo del Guerrero", "Incrementa en 220 el ataque de monstruos de tipo Guerrero.", "G", 220, "ataque"],
            ["Escudo del Lanzador", "Incrementa en 200 la defensa de monstruos de tipo Lanzador de Conjuros.", "L", 200, "defensa"],
            ["Espada del Zombi", "Incrementa en 170 el ataque de monstruos de tipo Zombi.", "Z", 170, "ataque"],
            ["Amuleto de Luz", "Incrementa en 150 el ataque de monstruos de tipo Lanzador de Conjuros.", "L", 150, "ataque"],
            ["Espada Oscura", "Incrementa en 220 el ataque de monstruos de tipo Demonio.", "O", 220, "ataque"],
            ["Escudo del Lanzador de Conjuros", "Incrementa en 180 la defensa de monstruos de tipo Lanzador de Conjuros.", "L", 180, "defensa"],
            ["Espada Demoníaca", "Incrementa en 250 el ataque de monstruos de tipo Demonio.", "O", 250, "ataque"],
            ["Escudo de Zombi", "Incrementa en 210 la defensa de monstruos de tipo Zombi.", "Z", 210, "defensa"]
        ]

        trampa = [
            ["Espejo de Oscuridad", "Impide el ataque de monstruos con atributo OSCURIDAD.", "OSCURIDAD"],
            ["Tornado de Polvo", "Detiene el ataque de monstruos con atributo VIENTO.", "VIENTO"],
            ["Escudo de Luz", "Impide el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Barrera de Fuego", "Detiene el ataque de monstruos con atributo FUEGO.", "FUEGO"],
            ["Fuerza del Viento", "Detiene el ataque de monstruos con atributo VIENTO.", "VIENTO"],
            ["Piedra del Guerrero", "Impide el ataque de monstruos con atributo TIERRA.", "TIERRA"],
            ["Luz Eterna", "Detiene el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Red de Oscuridad", "Impide el ataque de monstruos con atributo OSCURIDAD.", "OSCURIDAD"],
            ["Guardia del Dragón", "Detiene el ataque de monstruos con atributo AGUA.", "AGUA"],
            ["Puño de Fuego", "Impide el ataque de monstruos con atributo FUEGO.", "FUEGO"],
            ["Escudo de Tierra", "Detiene el ataque de monstruos con atributo TIERRA.", "TIERRA"],
            ["Viento Cortante", "Impide el ataque de monstruos con atributo VIENTO.", "VIENTO"],
            ["Reflejo de Luz", "Detiene el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Obsidiana Negra", "Impide el ataque de monstruos con atributo OSCURIDAD.", "OSCURIDAD"],
            ["Trampa Acuática", "Detiene el ataque de monstruos con atributo AGUA.", "AGUA"],
            ["Escudo Luminiscente", "Impide el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Espejo Ígneo", "Detiene el ataque de monstruos con atributo FUEGO.", "FUEGO"],
            ["Lluvia de Tierra", "Impide el ataque de monstruos con atributo TIERRA.", "TIERRA"],
            ["Resistencia del Dragón", "Detiene el ataque de monstruos con atributo AGUA.", "AGUA"],
            ["Sombra Oscura", "Impide el ataque de monstruos con atributo OSCURIDAD.", "OSCURIDAD"],
            ["Reflejo del Viento", "Detiene el ataque de monstruos con atributo VIENTO.", "VIENTO"],
            ["Escudo del Guerrero", "Impide el ataque de monstruos con atributo TIERRA.", "TIERRA"],
            ["Alma de Fuego", "Detiene el ataque de monstruos con atributo FUEGO.", "FUEGO"],
            ["Trampa Celestial", "Impide el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Red Venenosa", "Detiene el ataque de monstruos con atributo AGUA.", "AGUA"],
            ["Fuerza del Demonio", "Impide el ataque de monstruos con atributo OSCURIDAD.", "OSCURIDAD"],
            ["Luz de Dragón", "Detiene el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Puño del Zombi", "Impide el ataque de monstruos con atributo TIERRA.", "TIERRA"],
            ["Llamarada Infernal", "Detiene el ataque de monstruos con atributo FUEGO.", "FUEGO"],
            ["Defensa Profunda", "Impide el ataque de monstruos con atributo AGUA.", "AGUA"],
            ["Espíritu del Viento", "Detiene el ataque de monstruos con atributo VIENTO.", "VIENTO"],
            ["Escudo Áureo", "Impide el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Reflejo Gélido", "Detiene el ataque de monstruos con atributo AGUA.", "AGUA"],
            ["Rescate Oscuro", "Impide el ataque de monstruos con atributo OSCURIDAD.", "OSCURIDAD"],
            ["Viento Cortante", "Detiene el ataque de monstruos con atributo VIENTO.", "VIENTO"],
            ["Trampa de Rayo", "Impide el ataque de monstruos con atributo FUEGO.", "FUEGO"],
            ["Defensa Estelar", "Detiene el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Escudo Tóxico", "Impide el ataque de monstruos con atributo TIERRA.", "TIERRA"],
            ["Reflejo Solar", "Detiene el ataque de monstruos con atributo LUZ.", "LUZ"],
            ["Reversa del Dragón", "Impide el ataque de monstruos con atributo AGUA.", "AGUA"],
            ["Escudo Acuático", "Detiene el ataque de monstruos con atributo AGUA.", "AGUA"]
        ]


        # Crear cartas de monstruo a partir de los datos y agregarlas al mazo
        for carta in mounstruo:
            mazo.append(CartaMonstruo(carta[0], carta[1], carta[2], carta[3], carta[5], carta[4], True))

        for carta in magicas:
            mazo.append(CartaMagica(carta[0], carta[1], carta[2], carta[3], carta[4]))
        
        for carta in trampa:
            mazo.append(CartaTrampa(carta[0], carta[1], carta[2]))

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

class Tablero:
    def __init__(self):
        # Espacios de cartas: 3 para monstruos y 3 para mágicas/trampa
        self.zona_monstruos = [None] * 3
        self.zona_magica_trampa = [None] * 3
        self.turno = 1

    def agregar_carta_monstruo(self, carta):
        """
        Agrega una carta monstruo a la zona de monstruos.
        """
        if isinstance(carta, CartaMonstruo):
            for i in range(len(self.zona_monstruos)):
                if self.zona_monstruos[i] is None:
                    self.zona_monstruos[i] = carta
                    print(f"Carta {carta.nombre} colocada en la zona de monstruos en modo {'ataque' if carta.en_ataque else 'defensa'}.")
                    return True
        print("No hay espacio disponible en la zona de monstruos.")
        return False

    def agregar_carta_magica_o_trampa(self, carta):
        """
        Agrega una carta mágica o de trampa a la zona correspondiente.
        """
        if isinstance(carta, (CartaMagica, CartaTrampa)):
            for i in range(len(self.zona_magica_trampa)):
                if self.zona_magica_trampa[i] is None:
                    self.zona_magica_trampa[i] = carta
                    estado = "boca abajo" if isinstance(carta, CartaTrampa) else "boca arriba"
                    print(f"Carta {carta.nombre} colocada en la zona de mágicas/trampa ({estado}).")
                    return True
        print("No hay espacio disponible en la zona de mágicas/trampa.")
        return False

    def obtener_cartas_monstruo(self):
        """
        Devuelve las cartas de la zona de monstruos.
        """
        return [carta for carta in self.zona_monstruos if carta is not None]

    def obtener_cartas_magicas(self):
        """
        Devuelve las cartas mágicas de la zona mágica/trampa.
        """
        return [carta for carta in self.zona_magica_trampa if isinstance(carta, CartaMagica)]

    def obtener_cartas_trampa(self):
        """
        Devuelve las cartas trampa de la zona mágica/trampa.
        """
        return [carta for carta in self.zona_magica_trampa if isinstance(carta, CartaTrampa)]

    def mostrar_tablero_1(self, jugador, enemigo):
        """
        Muestra las cartas actuales en el tablero con un diseño mucho más grande.
        Este es el tablero de la persona (jugador).
        """
        MounstroZone = []
        for i, carta in enumerate(self.zona_monstruos):
            if carta and carta.en_ataque:
                MounstroZone.append(f"[{i + 1}] {carta}")
            elif carta:
                MounstroZone.append(f"[{i + 1}] Carta en modo defensa (boca abajo)")
            else:
                MounstroZone.append(f"[{i + 1}] (vacío)")

        MagicasTrampaZone = []
        for i, carta in enumerate(self.zona_magica_trampa):
            if carta:
                estado = "boca arriba" if not isinstance(carta, CartaTrampa) or not carta.boca_abajo else "boca abajo"
                MagicasTrampaZone.append(f"[{i + 1}] {carta} - ({estado})")
            else:
                MagicasTrampaZone.append(f"[{i + 1}] (vacío)")
            
            # Crear las zonas de cartas con numpy
        tablero = np.array([
            ["**Zona Monstruos**", *MounstroZone],  # Zona de Monstruos
            ["**Zona Mágica y Trampa**", *MagicasTrampaZone]  # Zona de Magia y Trampa
        ], dtype=object)

        # Definir el ancho de cada celda para alinearlo bien
        max_len = 30  # Ancho máximo para cada celda, ajustable según sea necesario

        # Imprimir el tablero de manera bonita con el título centrado
        print("-" * (max_len * 5))  # Línea superior para separar el tablero
        for i, row in enumerate(tablero):
            # Centrar los títulos
            if i == 0:  # Si es la primera fila (Zona Monstruos)
                print(f"{row[0]:^{max_len * 5}}")  # Centrado del título de la zona de monstruos
            elif i == 1:  # Si es la segunda fila (Zona Mágica y Trampa)
                print(f"{row[0]:^{max_len * 5}}")  # Centrado del título de la zona de magia y trampa
            # Imprimir las cartas alineadas
            print(" | ".join([str(cell).ljust(max_len) for cell in row[1:]]))  # Mostrar las cartas alineadas
            print("-" * (max_len * 5))  # Línea inferior para separar las cartas
        
        
        if isinstance(jugador, Jugador) and isinstance(enemigo, JugadorMaquina):
            print(" ")
        return f"Jugador 1: {jugador.vida}   Jugador 2: {enemigo.vida}\n" 
                
        

    def mostrar_tablero_2(self):
        """
        Muestra las cartas actuales en el tablero con un diseño mucho más grande.
        Este es el tablero del enemigo.
        """
        MounstroZone = []
        for i, carta in enumerate(self.zona_monstruos):
            if carta and carta.en_ataque:
                MounstroZone.append(f"[{i + 1}] {carta}")
            elif carta:
                MounstroZone.append(f"[{i + 1}] Carta en modo defensa (boca abajo)")
            else:
                MounstroZone.append(f"[{i + 1}] (vacío)")

        MagicasTrampaZone = []
        for i, carta in enumerate(self.zona_magica_trampa):
            if carta:
                estado = "boca arriba" if not isinstance(carta, CartaTrampa) or not carta.boca_abajo else "boca abajo"
                MagicasTrampaZone.append(f"[{i + 1}] {carta} - ({estado})")
            else:
                MagicasTrampaZone.append(f"[{i + 1}] (vacío)")

        # Crear las zonas de cartas con numpy
        tablero = np.array([
            ["**Zona Mágica y Trampa**", *MagicasTrampaZone],  # Zona de Magia y Trampa
            ["**Zona Monstruos**", *MounstroZone]  # Zona de Monstruos
        ], dtype=object)

        # Definir el ancho de cada celda para alinearlo bien
        max_len = 30  # Ancho máximo para cada celda, ajustable según sea necesario

        # Imprimir el tablero de manera bonita con el título centrado
        print("-" * (max_len * 5))  # Línea superior para separar el tablero
        for i, row in enumerate(tablero):
            # Centrar los títulos
            if i == 0:  # Si es la primera fila (Zona Monstruos)
                print(f"{row[0]:^{max_len * 5}}")  # Centrado del título de la zona de monstruos
            elif i == 1:  # Si es la segunda fila (Zona Mágica y Trampa)
                print(f"{row[0]:^{max_len * 5}}")  # Centrado del título de la zona de magia y trampa
            # Imprimir las cartas alineadas
            print(" | ".join([str(cell).ljust(max_len) for cell in row[1:]]))  # Mostrar las cartas alineadas
            print("-" * (max_len * 5))  # Línea inferior para separar las cartas
            
            
        return " "

    def eliminar_carta_monstruo(self, indice):
        """
        Elimina una carta monstruo de la zona de monstruos.
        """
        if 0 <= indice < len(self.zona_monstruos) and self.zona_monstruos[indice]:
            carta_eliminada = self.zona_monstruos[indice]
            self.zona_monstruos[indice] = None
            print(f"Carta {carta_eliminada.nombre} eliminada de la zona de monstruos.")
            return carta_eliminada
        print("No hay carta en la posición indicada.")
        return None

    def eliminar_carta_magica_trampa(self, indice):
        """
        Elimina una carta mágica o trampa de la zona correspondiente.
        """
        if 0 <= indice < len(self.zona_magica_trampa) and self.zona_magica_trampa[indice]:
            carta_eliminada = self.zona_magica_trampa[indice]
            self.zona_magica_trampa[indice] = None
            print(f"Carta {carta_eliminada.nombre} eliminada de la zona de mágicas/trampa.")
            return carta_eliminada
        print("No hay carta en la posición indicada.")
        return None

from enum import Enum

class TipoMonstruo(Enum):
    L = "Lanzador de Conjuros "
    D = "Dragón"
    Z = "Zombi "
    G = "Guerrero"
    B = "Bestia"
    O = "Demonio"


def main():
    # Crear una instancia de MazoCartas
    mazo_cartas = MazoCartas()
    
    # Cargar y seleccionar cartas desde el archivo
    mazo_jugador1 = mazo_cartas.seleccionar_mazo()
    mazo_jugador2 = mazo_cartas.seleccionar_mazo()
    
    # Crear jugadores
    jugador1 = Jugador("Jugador 1", mazo_jugador1)
    jugador2 = JugadorMaquina("Jugador Máquina", mazo_jugador2)
    
    # Función para mostrar un separador de turno
    def mostrar_separador_turno(turno, jugador):
        print("\n" + "=" * 40)
        print(f"              TURNO {turno}: {jugador}")
        print("=" * 40 + "\n")
    
    # Función para las fases
    def fase_tomar_carta(jugador):
        print("[FASE: TOMAR CARTA]")
        jugador.robar_carta()
        print(f"{jugador.nombre} roba una carta del mazo.\n")
    
    def fase_principal(jugador):
        print("[FASE: PRINCIPAL]")
        jugador.jugar_carta()
        print(f"{jugador.nombre} ha jugado una carta en su tablero.\n")
    
    def fase_batalla(jugador_atacante, jugador_defensor, turno):
        print("[FASE: BATALLA]")
        if turno == 1:
            print("No se puede declarar batalla en el primer turno.\n")
        else:
            jugador_atacante.declarar_batalla(jugador_defensor)
            print(f"{jugador_atacante.nombre} declara batalla.\n")
    
    # Inicializar turno
    turno = 1

    # Simular el juego
    while jugador1.vida > 0 and jugador2.vida > 0 and len(jugador1.mazo) > 0 and len(jugador2.mazo) > 0:
        # Turno del Jugador 1
        mostrar_separador_turno(turno, jugador1.nombre)
        fase_tomar_carta(jugador1)
        fase_principal(jugador1)
        print(jugador1.tablero.mostrar_tablero_2())
        print(jugador2.tablero.mostrar_tablero_1(jugador1, jugador2))
        fase_batalla(jugador1, jugador2, turno)
        
        jugador1.tablero.turno += 1
        jugador2.tablero.turno += 1

        if jugador2.vida <= 0:
            break  # Termina el juego si el Jugador 2 pierde

        # Turno del Jugador 2
        mostrar_separador_turno(turno + 1, jugador2.nombre)
        fase_tomar_carta(jugador2)
        fase_principal(jugador2)
        print(jugador1.tablero.mostrar_tablero_2())
        print(jugador2.tablero.mostrar_tablero_1(jugador1, jugador2))
        fase_batalla(jugador2, jugador1, turno + 1)
        
        jugador1.tablero.turno += 1
        jugador2.tablero.turno += 1

        if jugador1.vida <= 0:
            break  # Termina el juego si el Jugador 1 pierde

        # Incrementar turno
        turno += 2

    # Mostrar el ganador
    print("\n" + "=" * 40)
    if jugador1.vida > jugador2.vida:
        print(f"¡{jugador1.nombre} ha ganado el duelo!")
    elif jugador2.vida > jugador1.vida:
        print(f"¡{jugador2.nombre} ha ganado el duelo!")
    else:
        print("¡El duelo ha terminado en empate!")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    main()
