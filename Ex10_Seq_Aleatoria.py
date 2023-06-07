"""
Solicite ao usuário que digite cinco números, calcula a soma desses números e, em seguida, calcula a média. Por fim, imprima a soma e a média.
"""

soma = 0
qtd = 0
qtd_entrada = 1

while qtd_entrada <= 5:
    entrada = int(input("Digite um numero: "))
    soma = soma + entrada
    qtd = qtd + 1
    qtd_entrada = qtd_entrada + 1

media = soma / qtd
print(f"Soma: {soma}")
print(f"Média: {media}") 