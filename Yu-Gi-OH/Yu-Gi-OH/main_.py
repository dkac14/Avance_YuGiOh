from clases.MazoCartas import MazoCartas
from clases.Jugador import Jugador
from clases.JugadorMaquina import JugadorMaquina


def main():
    # Crear una instancia de MazoCartas
    mazo_cartas = MazoCartas()
    
    # Cargar y seleccionar cartas desde el archivo
    mazo_jugador1 = mazo_cartas.seleccionarMazo("Cartas.txt")
    mazo_jugador2 = mazo_cartas.seleccionarMazo("Cartas.txt")
    
    # Crear jugadores
    jugador1 = Jugador("Jugador 1", mazo_jugador1)
    jugador2 = Jugador("Jugador Máquina", mazo_jugador2)
    
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