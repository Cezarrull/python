numOne = float(input("Digite a primeira nota: "))
numTwo = float(input("Digite a segunda nota: "))
media = (numOne + numTwo) / 2

if media >= 5:
    print("Sua nota é", media, "você está aprovado")
else:
    print("Sua nota é", media, "você está reprovado")