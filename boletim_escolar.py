print("================================")
print("       BOLETIM ESCOLAR")
print("================================")

nome = input("Nome do aluno: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("\n================================")
print("          RESULTADO")
print("================================")

print("Aluno:", nome)
print("Média:", round(media, 2))

if media >= 7:
    print("Situação: APROVADO")
elif media >= 5:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")

print("================================")
