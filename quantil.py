
number = float(input("Escolha um número entre 100 e 1000:"))

#if number >= 100 and number <= 250:
#    print("Quartil 1°")
#if number > 250 and number <= 500:
#    print("Quartil 2°")
#if number > 500 and number <= 750:
#    print("Quartil 3°")
#if number > 750 and number <= 1000:
#    print("Quartil 4°")
#else:
#    print("Número fora do intervalo")

#########################################################

#if numbber >= 100 and number <= 1000:
#    if number < 250:
#        print("Quartil 1°")
#    else: 
#        if number < 500:
#            print("Quartil 2°")
#        else:
#            if number < 750:
#                print("Quartil 3°")
#            else:
#                print("Quartil 4°")
#else:
#    print("Número fora do intervalo")
#código mais ágil

#########################################################

if number >= 100 and number <= 1000:
    if number < 250:
        print("Quartil 1°")
    elif number < 500:
        print("Quartil 2°")
    elif number < 750:
        print("Quartil 3°")
    else:
        print("Quartil 4°")
else:
    print("Número fora do intervalo")

#########################################################