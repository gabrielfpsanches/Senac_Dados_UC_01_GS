# Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00.
# Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.

# Entrada de Dados

import math

tamanho = int(input("Informe o tamanho da área de pintura em metros quadadros: "))


# Processamento de Dados

latas = (tamanho/3)/18
latastotal = math.ceil(latas)
compra = latas*130


# Saída de Dados

print(f"Você precisará comprar {latastotal} lata(s) e o valor da compra será de R$ {compra:.2f} reais")