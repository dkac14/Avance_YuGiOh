from clases.MazoCartas import MazoCartas
from clases.jugador import Jugador


class Main:
    def __init__(self):
        # Crear el mazo desde el archivo 'cartas.txt'
        self.mazo = MazoCartas("CartasEnTexto.txt")
        self.jugadores = []
    
    def agregar_jugador(self, nombre):
        jugador = Jugador(nombre)
        self.jugadores.append(jugador)
        print(f"Jugador '{nombre}' añadido al juego.")

    def iniciar_juego(self):
        if len(self.jugadores) < 2:
            print("Se necesitan al menos dos jugadores para comenzar el juego.")
            return

        print("¡Iniciando el juego!")
        # Barajar el mazo antes de repartir
        self.mazo.barajar()
        
        # Repartir cartas iniciales (5 cartas por jugador)
        for jugador in self.jugadores:
            for _ in range(5):
                carta = self.mazo.robar_carta()
                if carta:
                    jugador.agregar_carta(carta)
                else:
                    print("No hay suficientes cartas en el mazo.")
                    return

        print("Cartas repartidas. ¡Que comience el duelo!")
        self.mostrar_manos()

    def mostrar_manos(self):
        print("\nEstado inicial de las manos:")
        for jugador in self.jugadores:
            print(f"Mano de {jugador.nombre}:")
            for carta in jugador.mano:
                print(carta)
            print()

    def jugar(self):
        # Iniciar el juego (carga inicial, reparto de cartas)
        self.iniciar_juego()
        
        # Aquí puedes añadir la lógica de los turnos del juego.
        print("\nTurnos no implementados. Aquí comenzaría la lógica del duelo.")

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear la instancia principal del juego
    juego = Main()

    # Añadir jugadores
    juego.agregar_jugador("Alice")
    juego.agregar_jugador("Bob")

    # Iniciar el juego
    juego.jugar()
