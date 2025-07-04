# Exercícios: Testes Unitários com Pytest

1. **Teste de string**  
   Dada a função `inverte_string(s)` que retorna a string invertida, escreva um teste unitário para verificar o funcionamento com diferentes entradas.

   ```python
   def inverte_string(s):
       return s[::-1]
   ```

2. **Teste de lista vazia**  
   Dada a função `primeiro_elemento(lista)` que retorna o primeiro elemento de uma lista ou `None` se a lista estiver vazia, escreva testes para ambos os casos.

   ```python
   def primeiro_elemento(lista):
       if lista:
           return lista[0]
       return None
   ```

3. **Teste de upper em string**  
   Dada a função `para_maiusculas(string)` que retorna a string em letras maiúsculas, teste se a função retorna corretamente para diferentes entradas.

   ```python
   def para_maiusculas(string):
       return string.upper()
   ```

4. **Teste de comparação de listas**  
   Dada a função `ordena_lista(lista)` que retorna a lista ordenada, escreva um teste para garantir que a lista é ordenada corretamente.

   ```python
   def ordena_lista(lista):
       return sorted(lista)
   ```

5. **Teste de número par**  
   Dada a função `eh_par(n)` que retorna `True` se o número for par e `False` caso contrário, escreva testes para números pares e ímpares.

   ```python
   def eh_par(n):
       return n % 2 == 0
   ```

6. **Teste de exceção em divisão**  
   Implemente uma função `divide(a, b)` que lança uma exceção ao dividir por zero. Escreva um teste unitário para garantir que a exceção é lançada corretamente.

7. **Teste de remoção de elemento em lista**  
   Implemente uma função `remove_elemento(lista, elemento)` que remove um elemento da lista. Escreva testes para verificar se o elemento foi removido e se a lista permanece correta.

8. **Teste de formato de email**  
   Crie uma função `valida_email(um_email)` que retorna True caso um email (string) contenha uma `@` e False caso não contenha.