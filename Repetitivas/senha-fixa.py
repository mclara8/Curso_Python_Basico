senhaCorreta = 2002

while True:
    senha = int(input("Digite a senha: "))
    if senha == senhaCorreta:
        print("Acesso permitido!")
        break
    else:
        print("Senha Inválida! Tente novamente: ")