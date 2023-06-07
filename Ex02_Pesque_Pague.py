"""
O regulamento de um pesque-pague define que se for pescado uma quantidade de peixes com peso superior a 50kg,o cliente deve pagar uma multa de R$ 4,00 por kg excedente. Faça um programa que solicita ao usuário o peso pescado, verifica se há excesso de peso e calcula a multa correspondente, exibindo os resultados caso haja excesso de peso. Caso contrário, exibe a mensagem "Peso ok".
"""

peso = float(input("Qual o peso pescado? \n"))
excesso = peso - 50
multa = 50 + (4 *(peso - 50))

if peso > 50:
    print(f"Excesso: {excesso:.2f} Kg,\nMulta: R$ {multa:.2f}.")
else:
    print("Peso ok")