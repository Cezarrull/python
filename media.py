#media de nota de aluno(sem peso)

name = input("Digite seu nome:")

numOne = float(input("Digite a primeira nota: "))
numTwo = float(input("Digite a segunda nota: "))

media = (numOne + numTwo) / 2

if media >= 5:
    print(name, "Sua nota é", media, "você está aprovado")
else:
    print(name, "Sua nota é", media, "você está reprovado")