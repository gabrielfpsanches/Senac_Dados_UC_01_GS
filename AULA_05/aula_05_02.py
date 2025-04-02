#  Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor

num = [10,2,3,5,6,20,50,77,4,15]

soma = sum(num)   # comando "sum" é a soma da lista
maior = max(num)  # comando "max" é o maior numero da lista
menor = min(num)  # comando "min" é o menor numero da lista
media = sum(num)/len(num)   # comando "sum" soma a lista e comando "len" divide pela a quantidade de numeros da lista

num.sort()   #  comando "sort" coloca a lista em ordem crescente
print(num)

num.sort(reverse=True)    #  comando "sort(reverse.True)" coloca a lista em ordem decrescente
print(num)

print(soma)
print(maior)
print(menor)
print(media)
