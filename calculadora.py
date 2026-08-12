print("=== CALCULADORA ===")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação: ")

if operacao == "1":
    resultado = numero1 + numero2
elif operacao == "2":
    resultado = numero1 - numero2
elif operacao == "3":
    resultado = numero1 * numero2
elif operacao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Não é possível dividir por zero.")
        resultado = None
else:
    print("Operação inválida.")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)
