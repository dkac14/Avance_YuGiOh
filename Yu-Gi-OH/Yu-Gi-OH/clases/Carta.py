class Carta:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def jugar_carta(self, posicion):
        pass

    def eliminar_carta(self, condicion):
        pass
    
    def __str__(self):
        return (f"{self.nombre}: {self.descripcion}\n")