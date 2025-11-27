class Teclado:
    def __init__(self, idioma, inalambrico):
        self.idioma = idioma
        self.inalambrico = inalambrico

class Computador:
    def __init__(self, marca, almacenamiento, teclado:Teclado = None):
        self.marca = marca
        self.almacenamiento = almacenamiento
        self.teclado =teclado if teclado else Teclado("Portugues", False)