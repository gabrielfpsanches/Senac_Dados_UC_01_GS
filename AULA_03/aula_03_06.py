# Entrada de Dados

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

# Processamento dos Dados

if n1 > n2 and n1 > n3:
    print(f"O maior valor é {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior valor é {n2}")
elif n3 > n1 and n3 > n3:
    print(f"O maior valor é {n3}")
else:
    print("Existem pelo menos dois valores iguais")
    

