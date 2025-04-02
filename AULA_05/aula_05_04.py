# Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado GABARITO com as seguintes respostas: A, B, B, D, E

# Entrada de Dados

prova = []
GABARITO = ["A", "B", "B", "D", "E"]
acerto = 0
erro = 0
n = 1


# Processamento de Dados

for i in range (5):
    prova.append(input(f"Informa a alternativa da {n}.a questão: ").upper())
    n += 1
    
for i in range(len(prova)):
    if prova[i] == GABARITO[i]:
        acerto += 1
    else:
        erro += 1


# Saída de Dados

print("\n As alternativas informadas foram:")
print(prova)
print("\n As alternativas corretas são:")
print(GABARITO)
print(f"\n Portanto voce acertou {acerto} e errou {erro} questões:")

