
from clases.MazoCartas import MazoCartas
from clases.CartaMonstruo import CartaMonstruo
from clases.Tablero import Tablero
from clases.Carta import Carta
from clases.Jugador import Jugador
from clases.JugadorMaquina import JugadorMaquina

def main():
    cartas = MazoCartas()
    lista_1 = cartas.seleccionarMazo("Cartas.txt")
    lista_2 = cartas.seleccionarMazo("Cartas.txt")

  
    jugador1 = Jugador("Chris", lista_1)
    jugadorMaquina =  JugadorMaquina("Juan", lista_2)

    turno = 1
    while jugador1.vida > 0 and jugadorMaquina > 0:
        jugadorMaquina.jugar_turno()
        jugador1.jugar_turno()
        if turno > 1:
            jugadorMaquina.declarar_batalla(jugador1)
            jugador1.declarar_batalla(jugadorMaquina)
main()