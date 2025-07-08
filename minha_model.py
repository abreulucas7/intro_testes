import sqlite3

def criar_tabela(conn):
    conn.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)')
    conn.commit()

def inserir_usuario(conn, nome):
    conn.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))
    conn.commit()

def buscar_usuarios(conn):
    cursor = conn.execute('SELECT nome FROM usuarios')
    
    lista_usuarios = list()

    for linha in cursor.fetchall():
        lista_usuarios.append(linha[0])
        
    return lista_usuarios