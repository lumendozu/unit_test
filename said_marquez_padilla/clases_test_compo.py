class Camara:
    def __init__ (self,tipo,megapixeles):
        self.tipo = tipo
        self.megapixeles = megapixeles
        

class Celular:
    def __init__ (self, marca, modelo,camara_principal : Camara, camara_ultra: Camara, camara_macro: Camara):
        self.modelo = modelo
        self.marca = marca
        self.camara_principal = camara_principal
        self.camara_ultra = camara_ultra
        self.camara_macro = camara_macro

    def totalmegapixeles(self):
        return(self.camara_principal.megapixeles +
                self.camara_ultra.megapixeles +
                self.camara_macro.megapixeles)
    
