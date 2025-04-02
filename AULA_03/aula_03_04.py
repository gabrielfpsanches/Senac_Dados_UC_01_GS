# Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:
# • Ter entre 16 e 69 anos.
# • Pesar mais de 50 kg.
# • Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)

# Entrada de Dados

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
peso = int(input("Digite o seu peso: "))
sono = int(input("Digite a duração do seu sono nas últimas 24h: "))

# Processamento dos Dados

if idade <= 15 or idade >= 70:
    print("Você precisa ter mais que 16 anos")
elif peso <= 49:
    print("Você precisa ter mais 50 Kg")
elif sono <= 5:
    print("Você precisa ter dormido por mais que 6 horas nas últimas 24h")
else:
    print("Você pode doar sangue!")
