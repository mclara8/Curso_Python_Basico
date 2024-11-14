import math

base = float(input("Digite o valor da base do retângulo: "))
altura = float(input("Digite o valor da altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt((altura ** 2) + (base ** 2))

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
