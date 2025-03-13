n = int(input("Digite um número:"))
nTwo = int(input("Digite a quantidade de números para encontrar os divisores:"))

for x in range(nTwo):
    if(x % n == 0):
        print(x)
    else: 
        print("Não é divisível por", n)