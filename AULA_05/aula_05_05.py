# Faça um programa que armazene em vetores o nome, a média e a situação de um grupo de 10 alunos. Ao final mostre o nome de cada aluno com sua respectiva situação.   

# Entrada de Dados
nomes = []
medias = []
situacoes = []

for i in range(10):
    nomes.append(input("Digite o nome do aluno: "))               # "append" vai guardando as informações
    medias.append(float(input("Digite a média do aluno: ")))

    if medias[i] >= 7:
        situacoes.append("Aprovado")   
    else:
        situacoes.append("Reprovado")

# Saída de Dados
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]} - Média: {medias[i]} - Situação: {situacoes[i]}")