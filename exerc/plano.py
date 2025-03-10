flat = int(input("Digite seu plano de trabalho: "))
wage = float(input("digite seu salário: ")) 

if flat == 1:
    newWage = 0.10 * wage
    print("O valor de seu salário atual sera de:", (newWage + wage))
elif flat == 2:
    newWage = 0.15 * wage
    print("O valor de seu salário atual sera de:", (newWage + wage))
elif flat == 3:
    newWage = 0.20 * wage
    print("O valor de seu salário atual sera de:", (newWage + wage))
else:
    print("Digite o valor correto do seu plano")