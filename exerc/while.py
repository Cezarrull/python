'''
n = int(input("Digite um n°:"))

maior = n
cont = 1

while(cont < 15):
    n = int(input("Digite um n°"))
    if(n > maior):
        maior = n
    cont + 1
    print(maior)
'''
#################################################

''''
num = int(input("Digite um n°:"))
menor = num

while num > 0:
    num = int(input("Digite um n°:"))
    if num < menor:
        menor = num
    print(menor)'
'''
num = int(input("Digite um n°:"))
menor = num

while num > 0:
    if num < menor:
        menor = num
    num = int(input("Digite um n°:"))
    print(menor)