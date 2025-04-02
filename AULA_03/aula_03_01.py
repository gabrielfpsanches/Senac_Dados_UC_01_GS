idade = int(input("informe a sua idade: "))
if idade < 18:
    print("Você é menor de idade")
elif idade ==18:
    print("Você tem exatos 18 anos - acesso liberado")
elif idade >=65:
    print("Você tem mais de 65 anos - Acesso liberado com cautela")
else:
    print("Acesso liberado")
