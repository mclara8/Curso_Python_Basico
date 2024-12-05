precoUnitario = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
pagamento = float(input("Dinheiro recebido: "))
valorTotal = precoUnitario * quantidade
troco = pagamento - valorTotal
diferenca = valorTotal - pagamento

if pagamento > valorTotal:
    print(f"TROCO =  {troco:.2f}")

if pagamento < valorTotal:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {diferenca:.2f} reais")