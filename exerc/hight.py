ladder = float(input("Digite a altura do degrau em centimetros: "))
hight = float(input("Digite a altura que deseja chegar em metros: "))

hightValue = hight*100

result = hightValue/ladder
valor = int(result)
if result-valor>.50: 
    valor=valor+1
    
print(f"\n\tNúmero de degraus: {valor} resultado= {result}")