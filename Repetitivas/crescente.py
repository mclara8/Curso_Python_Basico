x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

while x != y:
    if x < y:
        print("CRESCENTE")
    else:
        print("DECRESCENTE")
    break
