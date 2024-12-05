x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x < y and x < z:
    menor = x
elif y < z:
    menor = y
else:
    menor = z

print("O menor número é: ", menor)