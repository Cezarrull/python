#Leia um número inteiro e imprima resultado da diferença do seu triplo pelo dobro do seu sucessor

numOne = int(input("Digite um número inteiro"))

tri = numOne * 3
dob = (numOne + 1) * 2

result = tri - dob
print(result)