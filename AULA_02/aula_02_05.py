# Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é atemperatura em Celsius

# Entrada dos Dados

tempC = float(input("Digite a temperatura em graus Celsius: "))


# Processamento dos Dados

tempF = (9*tempC+160) / 5


# Saída de Dados
print (f"A temperatura em graus Fahrenheint é {tempF:.1f}")