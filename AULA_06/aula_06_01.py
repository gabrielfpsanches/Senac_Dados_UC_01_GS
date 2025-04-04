# Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) Quanto pagou ao IRRF.
# c) quanto pagou ao INSS.
# d) quanto pagou ao sindicato.
# e) o salário líquido.

# Entrada de Dados

nome = str(input("Informe o seu nome: "))
HT = float(input("Informe o valor da hora trabalhada por mês: "))
HM = int(input("Informe a quantidade de horas trabalhadas no mês: "))


salario = HT*HM
IR = (salario*11)/100
INSS = (salario*8)/100
sindicato = (salario*5)/100


print(f"Sr(a){nome}, você trabalhou por {HM} horas neste mês e o seu salário bruto deste mês foi de R${salario:.2f} reais")
print(f"\n Você será descontado no Imposto de Renda por R${IR:.2f} reais")
print(f"\n Você será descontado no INSS por R${IR:.2f} reais")
print(f"\n Você será descontado no sindicato por R${IR:.2f} reais")
print(f"O seu salário líquido deste mês foi de R${salario-(IR+INSS+sindicato)} reais")