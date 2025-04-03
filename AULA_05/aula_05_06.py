# Construa um programa que armazene em vetores o nome, a idade e o sexo de 10 pessoas. Ao final informe o nome da pessoa mais nova e da mais velha, a quantidade de pessoas maiores de idade e a quantidade de pessoas do sexo feminino.

# Entrada de Dados
nomes = []
idades = []
sexo = []

for i in range(10):
    nomes.append(input("Digite o nome da pessoa: "))         # "append" vai guardando as informações
    idades.append(int(input("Digite a idade da pessoa: ")))
    sexo.append(input("Digite o sexo da pessoa: "))

# Saída de Dados
maior_idade = idades[0]          # "[0]" cria uma atribuição inicial nas variáveis
menor_idade = idades[0]
qtd_sexo_F = 0
idade_maior = 0

for i in range(len(nomes)):
    if idades[i] > maior_idade:
        maior_idade = idades[i]
        maior_nome = nomes[i]
    
    if idades[i] < menor_idade:
        menor_idade = idades[i]
        menor_nome = nomes[i]
    
    if sexo[i] == "F" or sexo[i] == "f":
        qtd_sexo_F += 1

    if idades[i] >= 18:
        idade_maior += 1


print(f"Nome da pessoa mais nova: {menor_nome}")
print(f"Nome da pessoa mais velha: {maior_nome}")
print(f"Quantidade de pessoas maiores de idade: {idade_maior}")
print(f"Quantidade de pessoas do sexo feminino: {qtd_sexo_F}")


