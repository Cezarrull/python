number = float(input("Escolha um número entre 100 e 1000:"))

if number <= 250:
    print("Quantil 1°")
elif number > 250 and number <= 500:
    print("Quantil 2°")
elif number > 500 and number <= 750:
    print("Quantil 3°")
else:
    print("Quantil 4°")