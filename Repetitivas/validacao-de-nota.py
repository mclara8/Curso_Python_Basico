nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

while (nota1 > 0) and (nota2 > 0):
    media = (nota1 + nota2) / 2
    print(f"MÉDIA = {media:.2f}")
    break