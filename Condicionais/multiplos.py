numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

if (numero1 % numero2 == 0) or (numero2 % numero1 == 0):
    print("São múltiplos")
else:
    print("Não são múltiplos")