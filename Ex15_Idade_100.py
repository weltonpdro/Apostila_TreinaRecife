"""
Elabore um programa que receba varias idades. Encerre o recebimento quando receber uma idade com valor igual a 100. Ao final, exiba a maior idade recebida.
"""

maior_idade = -99

while True:
    idade = int(input("Digite uma idade: "))
    if idade == 100: break

    if idade > maior_idade:
        maior_idade = idade

print(f"A maior idade é: {maior_idade}")