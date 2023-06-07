"""
Solicite ao usuário um número inteiro e, em seguida, imprime todos os números ímpares menores que esse número. Por exemplo, se o usuário inserir 10, o programa imprimirá os números 1, 3, 5 e 7.
"""

n = int(input("Numero: "))
impar = 1

while impar < n:
    print(f"Impar: {impar}")
    impar = impar + 2