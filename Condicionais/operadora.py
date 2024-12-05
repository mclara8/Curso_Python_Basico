plano = 50.00
TAXA = 2.00
minutos = int(input("Digite a quantidade de minutos: "))

if minutos > 100:
    plano = plano + TAXA * (minutos - 100)

print(f"O valor final a ser pago será: R$ {plano:.2f}")