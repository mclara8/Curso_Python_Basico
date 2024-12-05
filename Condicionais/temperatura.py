escala = input("Você vai digitar a temperatura em qual escala (C/F)? ")

if escala == "F":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    conversaoCelsius = 5/9 * (fahrenheit - 32)
    print(f"Temperatura equivalente em Celsius: {conversaoCelsius:.2f}")

elif escala == "C":
    celsius = float(input("Digite a temperatura em Celsius: "))
    conversaoFahrenheit = 9 * celsius / 5 + 32
    print(f"Temperatura equivalente em Fahrenheit: {conversaoFahrenheit:.2f}")
