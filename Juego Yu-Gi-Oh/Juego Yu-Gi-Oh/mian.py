from .clases.MazoCartas import MazoCartas
from .clases.Jugador import Jugador
from .clases.JugadorMaquina import JugadorMaquina

def main():
    # Crear una instancia de MazoCartas
    mazo_cartas = MazoCartas()
    
    # Cargar y seleccionar cartas desde el archivo
    mazo_jugador1 = mazo_cartas.seleccionar_mazo()
    mazo_jugador2 = mazo_cartas.seleccionar_mazo()
    
    # Crear jugadores
    jugador1 = Jugador("Jugador 1", mazo_jugador1)
    jugador2 = JugadorMaquina("Jugador Máquina", mazo_jugador2)
    
    # Simular el juego:
    jugador1.robar_carta()
    jugador2.robar_carta()
    jugador2.tablero.turno += 1
    
    jugador1.jugar_carta()
    jugador2.jugar_carta()
    
    jugador1.declarar_batalla(jugador2)
    jugador2.declarar_batalla(jugador1)

    while jugador1.vida > 0 and jugador2.vida > 0 and len(jugador1.mazo) > 0 and len(jugador2.mazo) > 0:
        # Los jugadores roban una carta
        jugador1.robar_carta()
        jugador2.robar_carta()

        # Los jugadores juegan una carta
        jugador1.jugar_carta()
        jugador2.jugar_carta()

        # Los jugadores declaran batalla
        jugador1.declarar_batalla(jugador2)
        jugador2.declarar_batalla(jugador1)

if __name__ == "__main__":
    main()
