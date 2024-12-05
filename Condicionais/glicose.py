glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100:
    print("Classificação: Normal")
elif glicose <= 140:
    print("Classificação: Elevado")
elif glicose > 140:
    print("Classificação: Diabetes")

