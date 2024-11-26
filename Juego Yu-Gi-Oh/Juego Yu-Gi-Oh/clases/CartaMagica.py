from .Carta import Carta
from .CartaMonstruo import CartaMonstruo

class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, tipo_monstruo, incremento, tipo_incremento):
        super().__init__(nombre, descripcion)
        self.tipo_monstruo = tipo_monstruo
        self.incremento = incremento
        self.tipo_incremento = tipo_incremento
        self.equipada_a = None

    def activar_carta(self, monstruo):
        
        if not isinstance(monstruo, CartaMonstruo):
            print(f"{self.nombre} no puede equiparse porque el objetivo no es un monstruo.")
            return False

        if monstruo.tipo_monstruo == self.tipo_monstruo:
            self.equipada_a = monstruo
            if self.tipo_incremento == "ataque":
                monstruo.ataque += self.incremento
            elif self.tipo_incremento == "defensa":
                monstruo.defensa += self.incremento
            print(f"{self.nombre} equipada a {monstruo.nombre}. Incrementa su {self.tipo_incremento} en {self.incremento}.")
            return True
        else:
            print(f"{self.nombre} no puede equiparse a {monstruo.nombre} porque no es del tipo {self.tipo_monstruo}.")
            return False

    def destruir(self, lista_cartas, lista_monstruos):
        if self.equipada_a:
            if self.equipada_a not in lista_monstruos:
                print(f"{self.nombre} ha sido destruida porque {self.equipada_a.nombre} ya no está en el campo.")
                lista_cartas.remove(self)
                self.equipada_a = None


    def __str__(self):
        return (f"{self.nombre}: {self.descripcion}\n"
                f"Efecto: Incrementa {self.tipo_incremento} de monstruos tipo {self.tipo_monstruo} en {self.incremento}.")

