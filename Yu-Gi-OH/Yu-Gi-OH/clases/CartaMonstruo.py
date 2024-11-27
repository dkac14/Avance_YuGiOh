from .Carta import Carta




class CartaMonstruo(Carta):

    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo, elemento, modo):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo_monstruo = tipo_monstruo
        self.elemento = elemento
        self.en_ataque = modo

    # Métodos principales
    def atacar(self, carta_enemigo, lista_cartas_trampa, lista_carta_magica, puntos_vida_oponente, puntos_vida_atacante , lista_cartas_enemigo, lista_cartas_jugador, eleccion_atacantes, eleccion_defensor, tablero_atk, tablero_def):
        from .CartaTrampa import CartaTrampa
        from .CartaMagica import CartaMagica
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
        for i, carta_trampa in enumerate(lista_cartas_trampa):
            if isinstance(carta_trampa, CartaTrampa) and carta_trampa.verificar(self):
                carta_trampa.activar(self, lista_cartas_trampa, tablero_def, i)
                return puntos_vida_oponente

        # Continuar con el ataque si no hay trampas activadas
        if self.en_ataque:
            if carta_enemigo.en_ataque:
                # Ataque vs. Ataque
                if self.ataque > carta_enemigo.ataque:
                    print(f"{self.nombre} destruye a {carta_enemigo.nombre}.")
                    carta_enemigo.destruir(lista_cartas_enemigo)
                    tablero_def.eliminar_carta_monstruo(eleccion_defensor)
                    puntos_vida_oponente -= (self.ataque - carta_enemigo.ataque)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(lista_carta_magica):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == carta_enemigo:
                            carta_magica.destruir(lista_carta_magica, lista_cartas_enemigo)
                            tablero_def.eliminar_carta_magica_trampa(i)

                elif self.ataque < carta_enemigo.ataque:
                    print(f"{self.nombre} es destruido por {carta_enemigo.nombre}.")
                    self.destruir(lista_cartas_jugador)
                    tablero_atk.eliminar_carta_monstruo(eleccion_atacantes)
                    puntos_vida_atacante -= (carta_enemigo.ataque - self.ataque)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(lista_carta_magica):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == self:
                            carta_magica.destruir(lista_carta_magica, lista_cartas_jugador)
                            tablero_atk.eliminar_carta_magica_trampa(i)
                    
                    return puntos_vida_atacante

                else:
                    print(f"El ataque termina en empate. Los 2 monstruos son destruidos.")
                    print(f"{self.nombre} destruye a {carta_enemigo.nombre}.")
                    carta_enemigo.destruir(lista_cartas_enemigo)
                    tablero_def.eliminar_carta_monstruo(eleccion_defensor)
                    puntos_vida_oponente -= (self.ataque - carta_enemigo.ataque)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(lista_carta_magica):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == carta_enemigo:
                            carta_magica.destruir(lista_carta_magica, lista_cartas_enemigo)
                            tablero_def.eliminar_carta_magica_trampa(i)

                    print(f"{self.nombre} es destruido por {carta_enemigo.nombre}.")
                    self.destruir(lista_cartas_jugador)
                    tablero_atk.eliminar_carta_monstruo(eleccion_atacantes)
                    puntos_vida_atacante -= (carta_enemigo.ataque - self.ataque)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(lista_carta_magica):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == self:
                            carta_magica.destruir(lista_carta_magica, lista_cartas_jugador)
                            tablero_atk.eliminar_carta_magica_trampa(i)

            else:
                # Ataque vs. Defensa
                if self.ataque > carta_enemigo.defensa:
                    print(f"{self.nombre} destruye a {carta_enemigo.nombre} en modo defensa.")
                    carta_enemigo.destruir(lista_cartas_enemigo)
                    tablero_def.eliminar_carta_monstruo(eleccion_defensor)

                    # Gestionar cartas mágicas equipadas
                    for i, carta_magica in enumerate(lista_carta_magica):
                        if isinstance(carta_magica, CartaMagica) and carta_magica.equipada_a == carta_enemigo:
                            carta_magica.destruir(lista_carta_magica, lista_cartas_enemigo)
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
    def recibir_ataque_directo(self, puntos_vida_jugador, ataque):
        puntos_vida_jugador -= ataque
        print(f"{self.nombre} ataca de manera directa. El jugador pierde {ataque} puntos de vida.")
        return puntos_vida_jugador

    def __str__(self):
        modo = "Ataque" if self.en_ataque else "Defensa"
        return (f"{self.nombre} ({self.tipo_monstruo}/{self.elemento}) - "
                f"ATK: {self.ataque}, DEF: {self.defensa}")