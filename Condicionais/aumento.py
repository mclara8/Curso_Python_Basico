salario = float(input("Digite o salário do funcionário: "))

if salario <= 1000:
    aumento = salario * 0.20
    salario = salario + aumento
    print(f"Novo salário = R$ {salario:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 20%")

elif (salario > 1000) and (salario <= 3000):
    aumento = salario * 0.15
    salario = salario + aumento
    print(f"Novo salário = R$ {salario:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 15%")

elif (salario > 3000) and (salario <= 8000):
    aumento = salario * 0.10
    salario = salario + aumento
    print(f"Novo salário = R$ {salario:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 10%")

else:
    aumento = salario * 0.05
    salario = salario + aumento
    print(f"Novo salário = R$ {salario:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 5%")