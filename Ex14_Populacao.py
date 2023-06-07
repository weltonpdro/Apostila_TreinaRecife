"""
Considere dois países, A e B, cujas populações são fornecidas como entrada. O país A tem uma taxa de crescimento anual de 3%, enquanto o país B tem uma taxa de crescimento anual de 1.5%. Faça um programa que calcule e exiba quantos anos serão necessários para que a população do país A ultrapasse a população do país B.
"""

pop_a = int(input("População do país A: "))
pop_b = int(input("População do país B: "))

qtd_anos = 0

while pop_a < pop_b:
    pop_a = pop_a + (pop_a * 3/100)
    pop_b = pop_b + (pop_b * 1.5/100)

    qtd_anos = qtd_anos + 1

print(f"Total de anos: {qtd_anos}")