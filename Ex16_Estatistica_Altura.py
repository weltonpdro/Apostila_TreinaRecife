"""
O programa deve receber informações sobre a altura e o sexo(M ou F) de várias pessoas até que a palavra 'fim' seja digitada para encerrar a entrada de dados. Em seguida, o programa deve calcular e exibir:
a) a maior altura registrada;
b) a média da altura das mulheres;
c) a quantidade de homens registrados.
"""

maior_altura = 0
soma_alt_mulheres = 0
qtd_mulheres = 0
qtd_homens = 0

while True:
    sexo = input("Digite o sexo (M ou F): ")
    while sexo != "m" and sexo != "f" and sexo != "fim":
        print("Opção invalida")
        sexo = input("Digite o sexo (M ou F): ")
    if sexo == "fim": break
    altura = float(input("Digite a altura: "))

    if altura > maior_altura:
        maior_altura = altura
    if sexo == "f":
        qtd_mulheres = qtd_mulheres + 1
        soma_alt_mulheres = soma_alt_mulheres + altura
    else:
        qtd_homens = qtd_homens + 1

    if qtd_mulheres > 0:
        media_alt = soma_alt_mulheres / qtd_mulheres
    else:
        media_alt = 0

print(f"Maior altura: {maior_altura}")
print(f"Media da altura das mulheres: {media_alt}")
print(f"Qtd de homens: {qtd_homens}")