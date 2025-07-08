import pytest

# Função testada
def soma(a, b):
    return a + b


# TESTES Unitários
def test_soma1com1():
    assert soma(1,1) == 2

def test_soma1com0():
    assert soma(1,0) == 1

def test_soma_esquisita():
    with pytest.raises(TypeError):
        soma(10, "10")