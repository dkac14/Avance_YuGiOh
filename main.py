from classes import *

import random

class Main:
    @staticmethod
    def iniciar_juego():
        # Cargar las cartas desde archivo o definirlas directamente (simplificado para el ejemplo)
        cartas_monstruo = [
            CartaMonstruo("Dragón Blanco", "Un dragón poderoso", 3000, 2500, "D", "LUZ"),
            CartaMonstruo("Guerrero Oscuro", "Un guerrero tenaz", 1500, 1000, "G", "OSCURIDAD"),
            CartaMonstruo("Zombie Ancestral", "Un zombie que nunca muere", 1200, 1800, "Z", "TIERRA"),
        ]
        cartas_magicas = [
            CartaMagica("Espada de Arturo", "Incrementa ataque de Guerreros", "G", 200, "ataque"),
            CartaMagica("Escudo de Chamelote", "Incrementa defensa de Guerreros", "G", 200, "defensa"),
        ]
        cartas_trampa = [
            CartaTrampa("Tornado de Polvo", "Detiene ataques de atributo VIENTO", "VIENTO"),
        ]

        # Crear mazos para ambos jugadores
        deck_jugador = random.sample(cartas_monstruo, 20) + random.sample(cartas_magicas, 5) + random.sample(cartas_trampa, 5)
        random.shuffle(deck_jugador)

        deck_maquina = random.sample(cartas_monstruo, 20) + random.sample(cartas_magicas, 5) + random.sample(cartas_trampa, 5)
        random.shuffle(deck_maquina)

        # Crear jugadores
        jugador = Jugador("Jugador", deck_jugador)
        maquina = Jugador("Máquina", deck_maquina)

        # Iniciar el juego
        juego = Juego(jugador, maquina)
        juego.iniciar()

if __name__ == "__main__":
    Main.iniciar_juego()

