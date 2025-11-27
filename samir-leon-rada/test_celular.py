from celular import Celular, Bateria

def test_instancia_bateria():
    bat = Bateria(5000)
    cel = Celular("Samsung", bat)
    
    assert cel.bateria == bat 

def test_atributos():
    bat = Bateria(5000)
    cel = Celular("Xiaomi", bat)

    assert cel.marca == "Xiaomi"
    assert cel.bateria.capacidad == 5000

def test_metodo_capacidad():
    bat = Bateria(5000)
    cel = Celular("Motorola", bat)

    assert cel.obtener_capacidad_bateria() == 5000