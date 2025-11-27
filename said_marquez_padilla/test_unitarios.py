from clases_test import Biblioteca, Libro
from clases_test_compo import Celular, Camara
import pytest


# Agregacion
def test_estainstancia_libro():
    libro = Libro("El principuto", "Antoine de Saint-Exupéry", 1943)
    assert isinstance(libro,Libro)

def test_estainstancia_biblioteca():
    biblioteca = Biblioteca("El panorama")
    assert isinstance(biblioteca,Biblioteca)
    

def test_atributos_libro():
    libro = Libro("1984", "Jacki el pro", 1949)
    assert libro.titulo == "1984"
    assert libro.autor == "Jacki el pro"
    assert libro.fecha_publicacion == 1949

def test_atributos_biblioteca():
    biblioteca = Biblioteca("Biblioteca nacional")
    assert biblioteca.nombre == "Biblioteca nacional"


def test_agregar_libro():
    biblioteca = Biblioteca("La Gran Mundo")
    assert len(biblioteca.libros) == 0
    libro1 = Libro("Cien años de soledad", "Garcia Marquez", 1967)
    libro2 = Libro("Cronica de una muerte anunciada", "Garcia Marquez", 1981)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    assert len(biblioteca.libros) == 2
    
# Composicion

def test_instancia_celular():
    cam1 = Camara("principal", 108)
    cam2 = Camara("ultra angular", 48)
    cam3 = Camara("macro", 5)
    
    celular = Celular("Samsung", "S25 Ultra", cam1, cam2, cam3)
    assert isinstance(celular, Celular)

def test_celular_tiene_camara():
    cam_principal = Camara("principal", 200)
    cam_ultra = Camara("ultra angular", 50)
    cam_macro = Camara("macro", 8)

    celular = Celular("Apple", "iPhone 17 Pro", cam_principal, cam_ultra, cam_macro)

    assert isinstance(celular.camara_principal, Camara)
    assert celular.camara_principal.megapixeles == 200
    assert celular.camara_ultra.tipo == "ultra angular"
    assert celular.camara_macro.megapixeles == 8


def test_metodo_megapixeles():
    cam1 = Camara("Principal", 108)
    cam2 = Camara("Ultra angular", 48)
    cam3 = Camara("Macro", 12)

    celular = Celular("Samsung", "J2 Prime", cam1,cam2,cam3)
    assert celular.totalmegapixeles() == 168



