"""
Faça um programa que solicita ao usuário um nome com, no minimo, 10 caracteres. Com ele, você deve gerar uma senha no seguinte formato: divida o nome em duas partes, concatene os dois primeiros caracteres da segunda parte com os caracteres "%%", e os três ultimos caracteres da primeira parte. Ao final, exiba a parte 1, a parte 2 e a senha.
"""

nome = input("Digite um nome: ")

parte1 = nome[:len(nome)//2]
parte2 = nome[len(nome)//2:]

senha = parte2[:2] + "%%" + parte1[-3:]

print(f"Parte 1: {parte1}")
print(f"Parte 2: {parte2}")
print(f"Senha: {senha}")