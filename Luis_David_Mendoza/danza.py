# composicion.py

class Paso:
    def __init__(self, nombre, duracion_segundos):
        self.nombre = nombre
        self.duracion_segundos = duracion_segundos

class Coreografia:
    def __init__(self, titulo, estilo, paso_base: Paso):
        if not isinstance(paso_base, Paso):
            raise TypeError("El paso base debe ser una instancia de Paso")
        
        self.titulo = titulo
        self.estilo = estilo
        self.paso_base = paso_base 

    def mostrar_ritmo(self, velocidad):
        return f"La coreografia '{self.titulo}' se baila a velocidad {velocidad}"
