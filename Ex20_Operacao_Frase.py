"""
O programa deve receber uma frase como entrada do usuário e realizar algumas operações com ela:
a) os primeiros 5 caracteres;
b) os últimos 5 caracteres;
c) os primeiros 5 caracteres invertidos;
d) quantidade total de caracteres da frase."
"""

frase = input("Digite uma frase: ")
print(f"Os primeiros 5 caracteres: {frase[0:5]}")
print(f"Os ultimos 5 caracteres: {frase[-5:]}")
print(f"Os primeiros 5 caracteres da frase invertidos: {frase[::-5]}")
tam = len(frase)
print(f"Qtd de caracteres da frase: {tam}")