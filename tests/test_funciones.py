import pytest
from calculadora_grafica_funciones  import calculadora_raices, calculadora_vertice, agregar_a_csv, concavidad


def test_raices_dos_reales():
    assert calculadora_raices(1, -3, 2) in [(1.0, 2.0), (2.0, 1.0)]
    
def test_raiz_doble():
    assert calculadora_raices(1, -2, 1) in [(1.0, 1.0)]
    
def test_sin_raices_reales():
  assert calculadora_raices(-1, 0, -4) == "Error"
  
def test_vertice_correcto():
    assert calculadora_vertice(1, -4, 3) == (2.0, -1.0)

def test_concavidad():
  assert concavidad(3) == "Positiva"