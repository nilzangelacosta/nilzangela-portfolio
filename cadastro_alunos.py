print("=== CADASTRO DE ALUNO ===")

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade: "))
curso = input("Digite o curso: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("\n=== RESULTADO ===")
print("Nome:", nome)
print("Idade:", idade)
print("Curso:", curso)
print("Média:", round(media, 2))

if media >= 7:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")
