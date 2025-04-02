#  Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes. Some os dois valores se forem diferentes e multiplique-os se forem iguais

# Entrada de Dados
n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))

# Processamento de Dados

if n1 == n2:
    print(f"Eles são iguais. A soma do valor é {n1 + n2}")

else:
    print(f"Eles são diferentes. A multiplicação é {n1 * n2}")
