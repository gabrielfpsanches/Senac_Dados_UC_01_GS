# Programa Média

# Entrada de Dados
nome = input("Informe o nome do estudante: ")
n1 = float(input(f"Informe a primeira nota {nome}"))
n2 = float(input(f"Informe a segunda nota {nome}"))
n3= float(input(f"Informe a terceira nota {nome}"))

# Processamento dos dados
media = (n1+n2+n3)/3

# Saída dos dados
print(f"Se(a) {nome}, a sua média foi {media:.1f}")
