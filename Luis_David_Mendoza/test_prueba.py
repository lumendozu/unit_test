# test_danza.py
from bailarin import Bailarin, Compania
from danza import Coreografia, Paso


def test_instancias_compania():
    b1 = Bailarin("Lucia", "Contemporaneo")
    b2 = Bailarin("Omar", "Hip Hop")
    compania = Compania("Danza Viva", "Madrid")

    assert len(compania.bailarines) == 0
    
    compania.agregar_bailarin(b1)
    compania.agregar_bailarin(b2)

    assert len(compania.bailarines) == 2

    # Verificar bailarin 1 (indice 0)
    assert compania.bailarines[0].nombre == "Lucia"
    assert compania.bailarines[0].especialidad == "Contemporaneo"
    
    # Verificar bailarin 2 (indice 1)
    assert compania.bailarines[1].nombre == "Omar"
    assert compania.bailarines[1].especialidad == "Hip Hop"
    
    assert all(isinstance(b, Bailarin) for b in compania.bailarines)
    assert isinstance(compania, Compania)
    
def test_lista_compania():
    bailarin = Bailarin("Diana", "Jazz")
    compania = Compania("Compania Nacional", "Bogota")
    compania.agregar_bailarin(bailarin)
    
    assert bailarin in compania.bailarines

def test_atributos_compania():
    compania = Compania("Ballet Clasico", "Lima")
    assert compania.nombre == "Ballet Clasico"
    assert compania.ciudad == "Lima"



######################################################33

# test bailarion

def test_instancias_composicion():
    paso = Paso("Pirueta", 2.5)
    coreo = Coreografia("El Cisne", "Ballet", paso)

    assert isinstance(coreo, Coreografia)
    assert isinstance(paso, Paso)
    
def test_atributos_composicion():
    paso = Paso("Wave", 1.0)
    coreo = Coreografia("Robots", "Locking", paso)

    assert isinstance(coreo.paso_base, Paso) 
    
    assert coreo.paso_base.nombre == "Wave"
    assert coreo.paso_base.duracion_segundos == 1.0
    
    assert coreo.titulo == "Robots"
    assert coreo.estilo == "Locking"
    
def test_metodo_coreografia():
    paso = Paso("Salto", 0.5)
    coreo = Coreografia("Fuego Lento", "Salsa", paso)
    
    resultado_ritmo = coreo.mostrar_ritmo("rapida")
    assert resultado_ritmo == "La coreografia 'Fuego Lento' se baila a velocidad rapida"
