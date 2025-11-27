from programa_clases_agregacion import App, Tablet
from programa_clases_composicion import Teclado, Computador
import pytest

#Test de Agregacion
def test_instancia_app ():
    app = App("Instagram", 2)
    assert isinstance(app, App)

def test_instancia_tablet():
    tablet = Tablet("apple")
    assert isinstance(tablet, Tablet)

def test_have_atributos():
    app = App("Youtube", 3)
    assert app.nombre == "Youtube"
    assert app.descarga == 3

def test_have_apps():
    tablet = Tablet("samnsung")
    assert len(tablet.apps) == 0    
    app1 = App("Snapchat", 2)
    app2 = App("Chrome", 4)
    tablet.instalar(app1)
    tablet.instalar(app2)
    assert  hasattr(tablet, 'instalar')
    assert len(tablet.apps) == 2
    assert tablet.apps[0].nombre == "Snapchat"

#Test de Composicion

def test_istancia_comp():
    teclado2 = Teclado("Jap", False)
    lenovo = Computador("lenovo", "516gb", teclado2)
    assert lenovo.teclado == teclado2
    assert isinstance(lenovo.teclado, Teclado)

def test_have_atributos_comp():
    teclado1 = Teclado('ingles', True)
    hp = Computador("hp", "400gb", teclado1)
    assert hp.marca == "hp"
    assert hp.almacenamiento == "400gb"

def test_computadora_tiene_teclado():
    teclado3 = Teclado('español', True)
    pc = Computador("Dell", "512", teclado3)
    assert pc.teclado == teclado3
    assert hasattr(pc, "teclado")
    assert isinstance(pc.teclado, Teclado)