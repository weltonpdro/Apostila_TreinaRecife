"""
Elabore um programa que receba uma frase e exiba a quantidade de letras "a" existentes na frase e a frase invertida.
"""

frase = input("Digite uma frase: ")

qtd_a = frase.count("a")
frase_invertida = frase[::-1]

print(f"A frase: '{frase}' contem a quantidade {qtd_a} de letras 'a';")
print(f"A frase: '{frase}' invetida é: {frase_invertida}")