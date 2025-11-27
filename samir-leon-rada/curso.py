class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []

    def add_estudiante(self, est):
        if isinstance(est, Estudiante):
            self.estudiantes.append(est)

    def cantidad(self):
        return len(self.estudiantes)