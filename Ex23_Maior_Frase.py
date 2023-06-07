"""
Elabore um programa que receba 5 frases e ao final exiba a maior frase digitada.
"""

maior = -1
maior_frase = ""
for i in range(5):
    frase = input(f"Digite a {i+1}ª frase: ")
    tam = len(frase)

    if tam > maior:
        maior = tam
        maior_frase = frase

print(f"Maior frase: {maior_frase}")
