class CartaMagica:
    #constructor
    def __init__(self, nombre, descripcion, tipo_monstruo, incremento, tipo_incremento):
        
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo_monstruo = tipo_monstruo
        self.incremento = incremento
        self.tipo_incremento = tipo_incremento

    #recibe carta tipo mounstro para aplicar el efecto de la carta mágica
    def aplicar_efecto(self, monstruo):
        
        if monstruo.tipo == self.tipo_monstruo:
            if self.tipo_incremento == 'ataque':
                monstruo.ataque += self.incremento
            elif self.tipo_incremento == 'defensa':
                monstruo.defensa += self.incremento
            print(f"{self.nombre} aplicada a {monstruo.nombre}. {self.tipo_incremento.capitalize()} incrementado en {self.incremento}.")
        else:
            print(f"{self.nombre} no tiene efecto en {monstruo.nombre}.")

    def __str__(self):
        return f"{self.nombre}: {self.descripcion} (Incrementa {self.tipo_incremento} de {self.tipo_monstruo} en {self.incremento})"

# Ejemplo de uso
class Monstruo:
    def __init__(self, nombre, tipo, ataque, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - ATK: {self.ataque}, DEF: {self.defensa}"

# Crear una carta mágica y un monstruo
espada_de_arturo = CartaMagica("Espada de Arturo", "Incrementa en 200 el ataque de monstruos de tipo Guerrero.", "Guerrero", 200, "ataque")
guerrero_valiente = Monstruo("Guerrero Valiente", "Guerrero", 1500, 1200)
#prueba
espada_de_arturo.aplicar_efecto(guerrero_valiente)
print(guerrero_valiente)
