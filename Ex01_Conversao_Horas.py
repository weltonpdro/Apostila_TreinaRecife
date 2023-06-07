"""
Faça um programa que receba o tempo de duração de um evento em segundos e mostre-os em horas, minutos e segundos.
"""

qtds = int(input("Quantidade de segundos: "))

h = qtds // 3600 
resto = qtds % 3600
m = resto // 60 
s = resto % 60 

print(f"{h}:{m}:{s}")