# Testes


## Tipos de teste

- **Testes unitários**: Verificam o funcionamento de unidades isoladas do código, como funções ou métodos, garantindo que cada parte funcione corretamente de forma independente.

  ```python
  # Teste unitário
  def soma(a, b):
      return a + b

  def test_soma():
      assert soma(2, 3) == 5
  ```

- **Testes de integração**: Avaliam a interação entre diferentes módulos ou componentes do sistema, assegurando que eles funcionam juntos conforme esperado.

  ```python
  # Teste de integração
  def multiplica(a, b):
      return a * b

  def calcula(a, b):
      return soma(a, b) * multiplica(a, b)

  def test_calcula():
      assert calcula(2, 3) == 25  # (2+3) * (2*3) = 5*6 = 30
  ```

- **Testes de sistema**: Testam o sistema como um todo, simulando cenários reais de uso para garantir que todos os requisitos funcionais sejam atendidos.

  ```python
  # Teste de sistema
  def sistema(a, b):
      return calcula(a, b) > 0

  def test_sistema():
      assert sistema(2, 3) is True
  ```

- **Testes de regressão**: Garantem que alterações ou correções no código não introduzam novos bugs em funcionalidades já existentes.

  ```python
  # Teste de regressão
  def test_regressao_soma():
      assert soma(0, 0) == 0
      assert soma(-1, 1) == 0
  ```

- **Testes parametrizados**: Permitem rodar o mesmo teste com diferentes conjuntos de dados, facilitando a validação de múltiplos casos de uso.

  ```python
  # Teste parametrizado
  import pytest

  @pytest.mark.parametrize("a,b,resultado", [
      (1, 2, 3),
      (2, 3, 5),
      (10, 5, 15),
  ])
  def test_soma_parametrizado(a, b, resultado):
      assert soma(a, b) == resultado
  ```

- **Testes de exceção/erro**: Verificam se o código lida corretamente com situações inesperadas ou entradas inválidas, lançando as exceções apropriadas.

  ```python
  # Teste de exceção/erro
  import pytest

  def divide(a, b):
      if b == 0:
          raise ValueError("Divisão por zero!")
      return a / b

  def test_divide_erro():
      with pytest.raises(ValueError):
          divide(1, 0)
  ```

- **Testes de performance**: Avaliam o desempenho do código, como tempo de execução e uso de recursos, para identificar possíveis gargalos.

  ```python
  # Teste de performance
  import time

  def processamento_lento():
      time.sleep(0.1)
      return True

  def test_performance():
      inicio = time.time()
      assert processamento_lento() is True
      fim = time.time()
      assert fim - inicio < 0.2
  ```

## Testes Unitários (Unit Tests)

[Definition of a unit test](https://www.artofunittesting.com/definition-of-a-unit-test/)

> Um teste unitário é um trecho automatizado de código que invoca uma *unidade de trabalho* no sistema e depois verifica uma única suposição sobre o comportamento dessa unidade de trabalho.

Uma *unidade de trabalho* é um único caso de uso funcional lógico no sistema que pode ser invocado por alguma interface pública (na maioria dos casos). Uma unidade de trabalho pode abranger um único método, uma classe inteira ou várias classes que colaboram para atingir um único propósito lógico e verificável.

Um bom teste unitário é:

- Automatizável
- Tem controle total sobre todas as partes em execução (utilize mocks ou stubs para alcançar esse isolamento quando necessário)
- Pode ser executado em qualquer ordem, caso faça parte de vários outros testes
- Executa em memória (sem acesso a banco de dados ou arquivos, por exemplo)
- Retorna consistentemente o mesmo resultado (você sempre executa o mesmo teste, por isso não são usado números aleatórios, por exemplo; devemos deixar isso para testes de integração ou de faixa)
- Executa rapidamente
- Testa um único conceito lógico no sistema
- É legível
- É de fácil manutenção
- É confiável (quando você vê o resultado, não precisa fazer debug do código para conferir o resultado)

Acho que qualquer teste que não atenda a todos esses critérios é um teste de integração e deve ser colocado em seu próprio projeto de “testes de integração”.


## Planos de teste

Um plano de teste é um documento que descreve a estratégia, objetivos, recursos, cronograma e critérios para as atividades de teste de um projeto. Ele serve como guia para garantir que todos os requisitos do sistema sejam verificados e validados de forma sistemática.

### Exemplo de plano de teste

| Caso de Teste         | Objetivo                                | Entradas         | Passos                         | Resultado Esperado      |
|-----------------------|-----------------------------------------|------------------|-------------------------------|------------------------|
| Testar soma positiva  | Verificar soma de dois números positivos| a=2, b=3         | Chamar soma(2, 3)             | Retorna 5              |
| Testar soma zero      | Verificar soma com zero                 | a=0, b=5         | Chamar soma(0, 5)             | Retorna 5              |
| Testar divisão por zero | Verificar tratamento de erro           | a=1, b=0         | Chamar divide(1, 0)           | Lança ValueError       |
| Testar performance    | Garantir execução em menos de 0.2s      | -                | Chamar processamento_lento()  | Tempo < 0.2s           |

O plano de teste pode ser expandido conforme a complexidade do sistema, incluindo mais casos, critérios de aceitação, responsáveis e datas previstas.

## Tutorial: Teste de Integração com Banco de Dados (Python + SQLite)

A seguir, um exemplo de como criar um teste de integração usando Pytest, Python e SQLite:

### 1. Código de exemplo para manipulação do banco

```python
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
```

### 2. Teste de integração com Pytest

```python
import sqlite3
import pytest

from minha_model import criar_tabela, inserir_usuario, buscar_usuarios

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
```

**Explicação:**
- O fixture `conexao` cria um banco SQLite em memória para garantir isolamento dos testes.
- O teste insere dois usuários e verifica se ambos estão presentes no banco.
- Ao final, a conexão é fechada automaticamente.

Esse padrão pode ser adaptado para outros bancos de dados e cenários de integração.

### Explicação sobre fixture e a função `conexao()`

- **Fixture:** No Pytest, uma fixture é uma função especial que prepara algum recurso necessário para os testes, como conexões de banco, arquivos temporários ou configurações. Fixtures ajudam a garantir que cada teste tenha um ambiente controlado e isolado.
- **Função `conexao()`:** Esta função é uma fixture que cria uma conexão com um banco SQLite em memória, garantindo que cada teste use um banco limpo e temporário.
- **Uso do `yield`:** O `yield` é utilizado para retornar o objeto `conn` para o teste. Tudo que vem antes do `yield` é executado antes do teste (setup), e tudo que vem depois do `yield` é executado após o teste (teardown). Assim, após o teste terminar, a linha `conn.close()` é chamada automaticamente, fechando a conexão e liberando recursos.

```python
@pytest.fixture
def conexao():
    # Setup: cria conexão e tabela
    conn = sqlite3.connect(':memory:')
    criar_tabela(conn)
    yield conn  # Disponibiliza a conexão para o teste
    # Teardown: fecha a conexão após o teste
    conn.close()
```