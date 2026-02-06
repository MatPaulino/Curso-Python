n1 = float(input("Digite um numero:   "))
dob = n1 * 2

print(f"O dobro de {n1} é {dob}!")

print("=== Mini Calculadora ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Escolha uma operação (1 a 4):  ")
numero_1 = float(input("Digite o primeiro número:  "))
numero_2 = float(input("Digite o segundo número:  "))

if operacao == "1" :
    print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")

if operacao == "2" :
    print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")

if operacao == "3" :
    print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")

if operacao == "4" :
    print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")