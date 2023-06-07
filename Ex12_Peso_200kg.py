"""
Elabore um programa que receba pesos de pessoas aleatoriamente. Encerre o recebimento quando receber um peso com valor superior a 200kg. Ao final exibir o menor peso recebido.
"""

menor_Peso = 9999

while True:
    peso = float(input("Digite o peso: "))
    if peso > 200: break

    if peso < menor_Peso:
        menor_Peso = peso

print(f"O menor peso é: {menor_Peso}")