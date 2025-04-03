# Faça um programa que armazene em um vetor de 10 posições os votos de um candidato de acordo com a seguinte legenda:
# João Pé das Couves 10
# Antônio Magalhães 30
# Marina Torres 5
# Ao final informe a quantidade de votos de cada candidato e o nome do vencedor.

# Entrada de Dados
votos = []       # criação da lista "votos"

for i in range(10):
    votos.append(int(input("Digite o voto: ")))

# Saída de Dados
joao = 0
antonio = 0
marina = 0

for i in range(len(votos)):
    if votos[i] == 10:
        joao += 1
    elif votos[i] == 30:
        antonio += 1
    elif votos[i] == 5:
        marina += 1

if joao > antonio and joao > marina:
    print("Vencedor: João Pé das Couves")
elif antonio > joao and antonio > marina:
    print("Vencedor: Antônio Magalhães")
elif marina > joao and marina > antonio:
    print("Vencedor: Marina Torres")

