import sqlite3
import pytest

from model_tuv import criar_tabela, inserir_usuario, buscar_usuarios

@pytest.fixture
def conexao():
    # Cria um banco em memória para testes
    conn = sqlite3.connect(':memory:')
    criar_tabela(conn)
    yield conn
    conn.close()

def test_inserir_e_buscar_usuario(conexao):
    inserir_usuario(conexao, 'Ana')
    inserir_usuario(conexao, 'Pedro')
    usuarios = buscar_usuarios(conexao)
    assert 'Ana' in usuarios
    assert 'Pedro' in usuarios
    assert len(usuarios) == 2
