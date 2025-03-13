#for x in 23, 45, 67, 49:
#    print(x)

''' 
    23
    45
    67
    49
'''

#for x in 23, 45, 67, 49:
#    print(x, end=" ")
#    '''23 45 67 49 '''

n1 = int(input("Digite o valor inicial: "))
n = int(input("Digite a quantidade a ser lida:"))

contImpar = 0
somaPar = 0
cont = 0

for x in range(n1, n):
    if(x % 2 == 0):
        somaPar += x
    else:
        contImpar += 1
        cont += 1
    print("A soma dos pares é:", somaPar)
