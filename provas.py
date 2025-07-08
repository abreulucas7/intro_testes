# Teste unitário
def soma(a, b):
    return a + b

def multiplica(a, b):
    return f'{a * b}'

## As duas funções passam no teste unitário...
def test_multiplica():
    assert multiplica(2,3) == '6'

def test_soma():
    assert soma(2, 3) == 5

#...mas não passam no teste de integração
# por causa da incompatibilidade das interfaces

# Teste de integração

def calcula(a, b):
    return soma(a, b) * multiplica(a, b)

def test_calcula():
    assert calcula(2, 3) == 30
