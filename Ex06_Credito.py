"""
Um banco concederá um credito especial com juros de 2% aos seus clientes de acordo com o saldo medio do ultimo ano. Faça um programa que receva p saldo medio de umcliente e calcule o valor do credito de acordo coma tabela abaixo. Escreva na tela o valor do credito disponivel.

De 0 a 500     - Nenhum credito
De 501 a 1000  - 30% do valor do saldo medio
De 1001 a 3000 - 40% do valor do saldo medio
Acima de 3001  - 50% do valor do saldo medio
"""

saldo = float(input("Digite o saldo médio: "))

if saldo <= 500: p = 0
elif saldo <= 1000: p = 30
elif saldo <= 3000: p = 40
else: p = 50

credito = saldo * (p / 100)

novo_saldo = saldo + credito

print(f"Valor do crédito: R$ {credito:.2f}\nNovo Saldo: R$ {novo_saldo:.2f}")