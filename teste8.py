def valida_email(um_email):
    return '@' in um_email

def test_valida_email():
    assert valida_email("lgmaciel@senacrs.com.br") == True
    assert valida_email("lgmacielsenacrs.com.br") == False
    assert valida_email("@") == True
    assert valida_email("lgmaciel@") == True
