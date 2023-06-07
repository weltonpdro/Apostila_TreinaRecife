"""
Dada uma quantidade de termos especificada pelo usuário, o programa deve gerar e exibir uma sequência de Fibonacci. A sequência começa com os primeiros dois termos, que são 1 e 1, respectivamente.
"""

qtd_termos = int(input("Qtd de termos: "))
a = 1
b = 1
print(a)
print(b)
termo = 2
while termo < qtd_termos:
    c = a + b
    print(c)
    a = b
    b = c
    termo = termo + 1