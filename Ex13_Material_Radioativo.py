"""
Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a massa incial, faça um programa que determine o tempo necessario para que a massa se torne menor de 0.5g. Ao final, escreva a massa inicial, a massa final e o tempo calculado em segundos.
"""

massa_inicial = float(input("Massa inicial: "))

t = 0
massa_final = massa_inicial

while massa_final >= 0.5:
    massa_final = massa_final/2
    t = t + 50

print(f"Massa inicial: {massa_inicial}")
print(f"Massa final: {massa_final:.2f}")
print(f"Tempo: {t}s")