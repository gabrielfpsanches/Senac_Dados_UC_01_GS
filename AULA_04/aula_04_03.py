# Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final mostre a soma e a média das idades

# Entrada de Dados
soma = 0
maior_idade = 0
menor_idade = 200

# Processamento de Dados - Estrutura de Repetição
for i in range (3):
    nome = input("Informe o nome do usuário: ")
    idade = int(input("Informe a idade do usuário: "))
    soma = soma + idade
    if idade > maior_idade:
        maior_idade = idade
        maior_nome = nome

    if idade < menor_idade:
        menor_idade = idade
        menor_nome = nome

# Saída dos Dados
print(f"A soma das idades foi {soma} anos")
print(f"A média das idades foi {(soma / (i+1)):.2f} anos")
print(f"Sr(a) {maior_nome}, você possui {maior_idade} anos, sendo você a pessoa mais velha do grupo")
print(f"Sr(a) {menor_nome}, você possui {menor_idade} anos, sendo você a pessoa mais nova do grupo")


