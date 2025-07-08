def remove_elemento(lista, elemento):
    lista.remove(elemento)
    return lista


def test_remove_elemento():
    lista = [1,2,3,4,5,6,7,8]
    elemento = 5
    remove_elemento(lista, elemento)
    assert elemento not in lista

    
    