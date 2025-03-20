nota = float(input("Digite uma nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Digite uma nota: "))
print("Nota", nota, "válida!")