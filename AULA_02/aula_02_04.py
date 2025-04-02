# Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela

# Importando a biblioteca de data e hora
import datetime

# Entrada de Dados
data_atual = datetime.date.today()
anoatual = data_atual.year 
anonasc = int(input("Informe o ano de nascimento: "))

# Processamento dos Dados
idade = anoatual - anonasc

# Saída de Dados
print(f"A sua idade é {idade} anos")