class App:
    def __init__(self, nombre, descarga):
        self.nombre = nombre
        self.descarga = descarga

class Tablet:
    def __init__(self, marca):
        self.marca = marca
        self.apps = []
        
    def instalar(self, app):
        self.apps.append(app)
