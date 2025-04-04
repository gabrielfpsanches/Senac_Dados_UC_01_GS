# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.


# contador = 1
# tempmenor = 0
# tempmaior = 0
# mediatemp = 0

temperatura = []
contador = 0


temperatura.append(int(input("Digite a temperatura ou digite X para encerrar: ")))

while temperatura < 0 or temperatura >= 0:
    temperatura.append(int(input("Digite a temperatura: ")))
    contador += 1
#else temperatura == X or temperatura == x:
#    print("Temperaturas contabilizadas")


soma = sum(temperatura)   # comando "sum" é a soma da lista
tempmaior = max(temperatura)  # comando "max" é o maior numero da lista
tempmenor = min(temperatura)  # comando "min" é o menor numero da lista
media = sum(temperatura)/len(temperatura)   # comando "sum" soma a lista e comando "len" divide pela a quantidade de numeros da lista
