from app import suma, multiplicar  #Importa ambas funciones al inicio

def test_suma():
    assert suma(2, 2) == 4

def test_multiplicar():
    assert multiplicar(3, 3) == 9