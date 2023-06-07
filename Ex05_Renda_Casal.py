renda_h = float(input("Renda do homem: "))
renda_m = float(input("Renda da mulher: "))

renda_conj = renda_h + renda_m

if renda_conj <= 900: ir = 0
elif renda_conj <= 1500: ir = 10
elif renda_conj <= 2500: ir = 15
else: ir = 25

valor_ir = renda_conj * ir/100
renda_liq = renda_conj - valor_ir

print(f"Renda conjunta: R$ {renda_conj:.2f}")
print(f"Aliquota: {ir}%")
print(f"Valor do IR: R$ {valor_ir:.2f}")
print(f"Renda Liquida: R$ {renda_liq:.2f}")