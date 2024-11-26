from clases.MazoCartas import MazoCartas
from clases.Jugador import Jugador
from clases.JugadorMaquina import JugadorMaquina

def main():
    cartas = MazoCartas()
    lista_1 = cartas.seleccionarMazo("Cartas.txt")
    lista_2 = cartas.seleccionarMazo("Cartas.txt")


    jugador1 = Jugador("Chris", lista_1)
    jugadorMaquina =  JugadorMaquina("Juan", lista_2)



    turno = 1
    while jugador1.vida > 0 and jugadorMaquina.vida > 0:
        print(f"\nTurno {turno}:")
        print(f"{jugadorMaquina.nombre} coloca cartas en el tablero.")
        jugadorMaquina.jugar_turno()
        if turno >= 2:
            print(f"{jugadorMaquina.nombre} ataca con sus monstruos.")
            jugadorMaquina.declarar_batalla(jugador1)

        
        print(f"{jugador1.nombre} coloca cartas en el tablero.")
        jugador1.jugar_turno()
        if turno >= 2:
            print(f"{jugador1.nombre} ataca con sus monstruos.")
            jugador1.declarar_batalla(jugadorMaquina)


        print(f'Vida de {jugador1.nombre}: {jugador1.vida}')
        print(f'Vida de {jugadorMaquina.nombre}: {jugadorMaquina.vida}')
        turno += 1  



    if jugador1.vida <= 0:
        print(f"¡{jugadorMaquina.nombre} ha ganado el duelo!")
    elif jugadorMaquina.vida <= 0:
        print(f"¡{jugador1.nombre} ha ganado el duelo!")
    else:
        print("- El duelo terminó en empate")
main()