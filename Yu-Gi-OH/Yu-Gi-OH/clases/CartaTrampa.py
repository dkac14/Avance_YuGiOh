from .Carta import Carta

class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, tipo_atributo):
        super().__init__(nombre, descripcion)
        self.tipo_atributo = tipo_atributo
        self.boca_abajo = True 

    def verificar(self, carta_atacante):
        verificacion = carta_atacante.elemento == self.tipo_atributo
        return verificacion

    def activar(self, carta_atacante, lista_cartas, tablero, indice):
        from .CartaMonstruo import CartaMonstruo
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
        estado = "Boca abajo" if self.boca_abajo else "Revelada"
        return f"{self.nombre} Atributo: {self.tipo_atributo}"
