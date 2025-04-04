# Crie um programa que:
# 1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
# 2- Exiba a lista completa.
# 3- Exiba o maior e o menor número da lista.
# 4- Exiba a soma e a média de todos os números.


num = []
n = 1



for i in range(10):    
    num.append(int(input("Informe os números: ")))
    n += 1

soma = sum(num)   # comando "sum" é a soma da lista
maior = max(num)  # comando "max" é o maior numero da lista
menor = min(num)  # comando "min" é o menor numero da lista
media = sum(num)/len(num)


print(f"\nA lista dos números são: {num}")   #consertar

print(f"\nO maior número é {maior}")

print(f"\nO menor número é {menor}")

print(f"\nA soma dos números é {soma}")

print(f"\nA média dos números é {media}")


