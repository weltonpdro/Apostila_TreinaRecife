"""
Faça um programa que receba três valores inteiros e exiba-os em ordem crescente, do menor para o maior.
"""

maior = -1
menor = 99999

v1 = int(input("Defina o primero valor: "))
v2 = int(input("Defina o segundo valor: "))
v3 = int(input("Defina o terceiro valor: "))

if v1 > maior: maior = v1
if v2 > maior: maior = v2
if v3 > maior: maior = v3

if v1 < menor: menor = v1
if v2 < menor: menor = v2
if v3 < menor: menor = v3

medio = (v1 + v2 + v3) - (menor + maior)
print(f"Sequencia em ordem crescente: {menor}, {medio} e {maior}")