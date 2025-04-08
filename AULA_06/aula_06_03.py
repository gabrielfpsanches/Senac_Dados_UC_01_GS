# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.

temperaturas = []

# Loop para ler as temperaturas
while True:
    entrada = input("Digite uma temperatura (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        break
    
    temperatura = float(entrada)
    
    temperaturas.append(temperatura)

if len(temperaturas) > 0:
    # Calcula a menor e a maior temperatura
    menor_temperatura = min(temperaturas)
    maior_temperatura = max(temperaturas)
    
    # Calcula a média das temperaturas
    media_temperaturas = sum(temperaturas) / len(temperaturas)
    
    # Exibe os resultados
    print(f"A menor temperatura é: {menor_temperatura}")
    print(f"A maior temperatura é: {maior_temperatura}")
    print(f"A média das temperaturas é: {media_temperaturas}")
else:
    print("Nenhuma temperatura foi registrada.")
