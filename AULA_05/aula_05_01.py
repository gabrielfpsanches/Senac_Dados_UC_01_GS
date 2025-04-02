nomes = "Alessandro, Maria, Eduarda"
nomes_lista = ["Alessandro", "Maria", "Eduarda"]
num = []  # lista vazia para inclusão de dados

for i in range(5):    # repete 5 vezes
    num.append(int(input("Informe um valor inteiro: ")))   # comando "append" para inserir

for i in range(len(num)):  # comando "len" para saber o tamanho da lista
    print(f"O número {num[i]} está na posição {i} da lista ")


print(num)
print("---------------")
print(nomes)
print(nomes_lista)
print(nomes_lista[2])  # informa a posição 2 da lista
