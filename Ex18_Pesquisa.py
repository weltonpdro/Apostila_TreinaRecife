"""
Um questionário foi aplicado a várias pessoas para coletar informações sobre um novo produto lançado no mercado. O questionario pergunta sobre sexo e se a pessoa gostou ou não do novo produto. O programa deve registrar e calcular algumas estatísticas com base nas respostas fornecidas até que a palavra 'fim' seja digitada. Em seguida, ele calcula e exibe:
a) a quantidade de pessoas que responderam 'sim';
b) a quantidade de pessoas que responderam 'nao';
c) o percentual de mulheres que responderam 'sim' em relação ao total de mulheres;
d) o percentual de homens que responderam 'nao' em relação ao total de respostas.
"""

qtd_sim = 0
qtd_nao = 0 
qtd_mulheres = mulheres_sim = 0
qtd_homens_nao = 0

while True:
    sexo = input("Informe o sexo (m, f, fim): ")
    while sexo != "m" and sexo != "f" and sexo != "fim":
        print("Erro: Sexo inválido")
        sexo = input("Informe o sexo (m, f, fim): ")
    if sexo == "fim": break

    resposta = input("Resposta (sim ou nao): ")
    while resposta != "sim" and resposta != "nao":
        print("Erro: Resposta Inválida")
        resposta = input("Resposta (sim ou nao)")

    if resposta == "sim":
        qtd_sim = qtd_sim + 1
    else:
        qtd_nao = qtd_nao + 1 

    if sexo == "f":
       qtd_mulheres = qtd_mulheres + 1  
       if resposta == "sim":
          mulheres_sim = mulheres_sim + 1
    else:
        if resposta == 'nao':
            qtd_homens_nao = qtd_homens_nao + 1

print(f"Qtd que responderam SIM: {qtd_sim}")
print(f"Qtd que responderam NÃO: {qtd_nao}")

perc_m = mulheres_sim * 100 / qtd_mulheres

print(f"Percentual letra c: {perc_m:.0f}%")

perc_h = qtd_homens_nao * 100 / (qtd_sim + qtd_nao)

print(f"Percentual letra d: {perc_h:.0f}%")