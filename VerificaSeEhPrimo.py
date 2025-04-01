num = int(input("Digite um número: "))
ehPrimo = True

if num<=1:
    ehPrimo= False
else:
    for i in range(2, int(num/2)+1):
        if num%i != 0:
            ehPrimo = True
        else:
            ehPrimo = False
            break

if ehPrimo:
    print("É primo!")
else:
    print("Não é primo!")







