import random
from clases.Carta import Carta
from clases.CartaMonstruo import CartaMonstruo
from clases.CartaMagica import CartaMagica
from clases.CartaTrampa import CartaTrampa
from clases.Tablero import Tablero
from clases.jugador import Jugador
from clases.JugadorMaquina import JugadorMaquina
from clases.MazoCartas import MazoCartas
from enums.elemento import Elemento
from enums.tipo_monstruo import TipoMonstruo

def main():
    # Crear una instancia de MazoCartas
    mazo_cartas = MazoCartas()
    
    # Cargar y seleccionar cartas desde el archivo
    ruta_archivo = "CartasEntexto.txt"
    mazo_jugador1 = mazo_cartas.seleccionarMazo(ruta_archivo)
    mazo_jugador2 = mazo_cartas.seleccionarMazo(ruta_archivo)
    
    # Crear jugadores
    jugador1 = Jugador("Jugador 1", mazo_jugador1)
    jugador2 = JugadorMaquina("Jugador Máquina", mazo_jugador2)
    
    # Simular el juego
    for _ in range(5):
        jugador1.robar_carta()
        jugador2.robar_carta()
    
    jugador1.jugar_carta()
    jugador2.jugar_carta()
    
    jugador1.declarar_batalla()
    jugador2.declarar_batalla()

if __name__ == "__main__":
    main()