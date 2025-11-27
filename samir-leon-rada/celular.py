class Bateria:
    def __init__(self, capacidad):
        self.capacidad = capacidad

class Celular: 
    DEFAULT_BATTERY_CAPACITY = 5000

    def __init__(self, marca, bateria):
        self.marca = marca
        self.bateria = bateria

    def obtener_capacidad_bateria(self):
        return self.bateria.capacidad