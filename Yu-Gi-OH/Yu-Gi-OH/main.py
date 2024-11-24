
from clases.Jugador import Jugador
from clases.MazoCartas import MazoCartas
from clases.CartaMonstruo import CartaMonstruo


def main():
    cartas = MazoCartas()
    lista = cartas.cargar_cartas("Cartas.txt")
    print(len(lista))

main()
