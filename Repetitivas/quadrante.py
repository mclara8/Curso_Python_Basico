x = int(input("Digite o valor da coordenada X: "))
y = int(input("Digite o valor da coordenada Y: "))

while (x != 0) and (y != 0):
    if (x < 0) and (y > 0):
        print("Quadrante 1")
    if (x > 0) and (y > 0):
        print("Quadrante 2")
    if (x < 0) and (y < 0):
        print("Quadrante 3")
    if (x > 0) and (y < 0):
        print("Quadrante 4")
    break
