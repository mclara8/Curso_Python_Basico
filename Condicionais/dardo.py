distancia1 = float(input("Digite a primeira distância: "))
distancia2 = float(input("Digite a segunda distância: "))
distancia3 = float(input("Digite a terceira distância: "))

if distancia1 > distancia2 and distancia1 > distancia3:
    print(f"MAIOR DISTÂNCIA = {distancia1:.2f}")
elif distancia2 > distancia3:
    print(f"MAIOR DISTÂNCIA = {distancia2:.2f}")
else:
    print(f"MAIOR DISTÂNCIA = {distancia3:.2f}")