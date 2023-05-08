number1 = int(input('Введите стартовое число: '))
number2 = int(input('Введите число разность между числами: '))
number3 = int(input('Введите количество числел : '))
def sum (A, B, C):
    mass = []
    i = 0
    while(i < C):
        mass.append(A)
        A = A + B
        i += 1
    print(mass)    
sum (number1, number2, number3) 