# Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida e no tempo em que uma viagem foi realizada

#Com base nos dados obtidos no programa anterior e sabendo que o veículo usado consome 12 Km/l, construa um programa que determine a quantidade de combustível gasto nessa viagem

# Entrada de Dados

deslocamento = float(input("Digite a distância percorrida em Km: "))
tempo = float(input("Digite o tempo percorrido em minutos: "))

# Processamento dos Dados
velmedia = deslocamento/tempo
combustivelgasto = deslocamento/12


# Saída de Dados
print(f"A velocidade média é {velmedia:.1f} Km/h")
print(f"A quantidade de combustível gasto é {combustivelgasto:.1f}: litros")