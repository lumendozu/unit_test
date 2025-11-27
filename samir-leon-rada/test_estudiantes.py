from curso import Curso, Estudiante

def test_instancia_estudiante():
    est = Estudiante("Samir")
    assert isinstance(est, Estudiante)

def test_add_y_cantidad():
    curso = Curso()
    assert curso.cantidad() == 0
    
    est1 = Estudiante("Ana")
    est2 = Estudiante("Juan")

    curso.add_estudiante(est1)
    curso.add_estudiante(est2)

    assert curso.cantidad() == 2

def test_atributos():
    est = Estudiante("Pedro")
    assert est.nombre == "Pedro"