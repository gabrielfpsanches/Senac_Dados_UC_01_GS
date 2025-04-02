# Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes condições:
# - Se a média for maior igual a 70 -> ATENDIDO
# - Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
# - Se a média for menor que 30 -> NÃO ATENDIDO

# Entrada de Dados
for i in range(3):
    nome = input("Informe o nome do aluno: ")
    n1 = float(input(f"Informe a primeira nota do aluno {nome}: "))
    n2 = float(input(f"Informe a segunda nota do aluno {nome}: "))

    media = (n1 + n2) / 2

    if media >= 70:
        situacao = "Atendido"
    elif media >= 30 and media < 70:
        situacao = "Parcialmente atendido"
    else:
        situacao = "Não atendido"

    print(f"Sr(a) {nome}, a sua média foi {media:.2f}, portanto você está {situacao}")


