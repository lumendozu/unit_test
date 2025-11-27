# bailarin.py
#agregacion

class Bailarin:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad 

class Compania:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.bailarines = [] 

    def agregar_bailarin(self, bailarin: Bailarin):
        if isinstance(bailarin, Bailarin):
            self.bailarines.append(bailarin)
