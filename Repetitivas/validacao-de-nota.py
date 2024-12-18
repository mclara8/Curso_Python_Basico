while True:
    nota1 = float(input("Digite a primeira nota: "))
    if (nota1 >= 0) and (nota1 <= 10):
        break
    else:
        print("Valor Inválido! Tente novamente.")

while True:
    nota2 = float(input("Digite a segunda nota: "))
    if (nota2 >= 0) and (nota2 <= 10):
        break
    else:
        print("Valor Inválido! Tente novamente")

media = (nota1 + nota2) / 2
print(f"MÉDIA = {media:.2f}")


