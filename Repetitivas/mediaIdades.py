nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

mediaIdades = (idade1 + idade2) / 2

print("DADOS DA PRIMEIRA PESSOA")
print("Nome: ", nome1)
print("Idade: ", idade1)

print("DADOS DA SEGUNDA PESSOA")
print("Nome: ", nome2)
print("Idade: ", idade2)

print("A idade média de", nome1, "e", nome2, "é de", mediaIdades, "anos")