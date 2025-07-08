import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        resultado = a/b
        return resultado

def test_divide():
    assert divide(10, 5) == 2.0
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

