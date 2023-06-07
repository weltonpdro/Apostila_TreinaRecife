"""
Solicite ao usuário que digite números até que o valor 999 seja inserido. Em seguida, calcula e imprime a quantidade de números digitados, a soma de todos os números e, se houver, a média dos números pares.
"""

qtd_numeros = 0
soma = 0 
soma_par = qtd_par = 0

while True :
    n = float(input("Digite um valor: "))
    if n == 999: break
    qtd_numeros = qtd_numeros + 1 
    soma = soma + n 

    resto = n % 2
    if resto == 0 :
        qtd_par = qtd_par + 1
        soma_par = soma_par + n

print(f"Quantidade de numeros: {qtd_numeros}.")
print(f"Soma dos numeros: {soma}.")

if qtd_par != 0 :
    media = soma_par / qtd_par
    print(f"Média dos pares: {media:.2f}.")
else:
    print("Não foram digitados numeros pares.")