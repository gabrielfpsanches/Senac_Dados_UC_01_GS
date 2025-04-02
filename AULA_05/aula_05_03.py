# Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos números são pares e quantos são ímpares e mostre o vetor principal na ordem inversa e depois na ordem crescente.

num = []
n = 1
qtd_par = 0
qtd_impar = 0
num_par = []
num_impar = []


for i in range(10):    
    num.append(int(input(f"Informe o {n}o. valor: ")))
    n += 1
    if num[i] % 2 == 0:
        num_par.append(num[i])
        qtd_par += 1
    else:
        num_impar.append(num[i])
        qtd_impar += 1

print(f"\nA quantidade de números pares é {qtd_par}")
print(num_par)
print(f"\nA quantidade de números ímpares é {qtd_impar}")
print(num_impar)


num.reverse()
print("\nLista em ordem reversa")       # "\n" comando para salto de linha e organização
print(num)

num.sort()
print("\nLista em ordem crescente")   
print(num)
