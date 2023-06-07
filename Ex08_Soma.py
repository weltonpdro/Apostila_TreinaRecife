"""
Faça um programa que solicita ao usuário um número inteiro e, em seguida, calcula a soma de todos os números de 1 até esse número. No final, ele exibe o valor da soma.
"""

n = int(input("Digite um numero: "))
soma = 0 
parcela = 1

while parcela <= n:
    soma = soma + parcela
    parcela = parcela + 1

print(f"Soma: {soma}")