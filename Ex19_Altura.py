"""
Faça um programa que receba a altura e sexo de 10 pessoas. Ao final, escreva a menor altura do grupo e a média da altura dos meninos. 
"""

soma_altura_meninos = 0
qtd_meninos = 0
menor_altura = float("inf")

for i in range(1, 6):
    sexo = input(f"Digite o sexo da {i}ª pessoa (M ou F): ")
    altura = float(input(f"Digite a altura da {i}ª pessoa: "))

    if altura < menor_altura:
        menor_altura = altura
    if sexo.upper() == "M":
        soma_altura_meninos = soma_altura_meninos + altura
        qtd_meninos = qtd_meninos + 1

if qtd_meninos > 0:
    media = soma_altura_meninos / qtd_meninos
else:
    media = 0

print(f"A menor altura do grupo: {menor_altura} m;")
print(f"A media da altura dos meninos é de {media} m.")