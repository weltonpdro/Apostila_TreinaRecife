"""
Elabore um programa que receba um numero inteiro e exiba a tabuada desse numero.
"""

n = int(input("Digite um valor: "))
p = 0

while p <= 10:
    print(f"{n} x {p} = {n * p}")
    p = p + 1