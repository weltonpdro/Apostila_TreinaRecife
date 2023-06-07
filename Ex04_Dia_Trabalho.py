"""
Um programa foi criado para calcular o novo valor do salário com base em um reajuste salarial. Se o salário for menor que R$ 1.100,00, significa que está na primeira faixa e o programa define o percentual de reajuste como 10% de aumento, enquanto os que recebem até R$ 2.000,00 terão reajuste de 7% de aumento. Se o salário não se encaixar em nenhuma das faixas anteriores, o programa define o percentual de reajuste como 5% de aumento.
"""

salario = float(input("Digite o valor do salario: \n"))

if salario < 1100: p = 1.1
elif salario < 2000: p = 1.07
else: p = 1.05

novo_salario = salario * p

print(f"O novo salario será de: R$ {novo_salario:.2f}.")