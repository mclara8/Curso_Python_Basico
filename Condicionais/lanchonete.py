produtos = [
    {"id": 1, "preco": 5.00},
    {"id": 2, "preco": 3.50},
    {"id": 3, "preco": 4.80},
    {"id": 4, "preco": 8.90},
    {"id": 5, "preco": 7.32}
]

codigoProduto = int(input("Código do produto comprado: "))
quantidade = int(input("Quantidade comprada: "))

for produto in produtos:
    if produto["id"] == codigoProduto:
        valorTotal = produto["preco"] * quantidade
        print(f"Valor a pagar: R$ {valorTotal:.2f}")