from random import randint
number = int(input('Введите количество элементов в массиве: '))
mass = []
for i in range(number):
    mass.append(randint(0, 11))     
print(mass)    
start = int(input('Введите начало диапазона: '))    
end = int(input('Введите конец диапазона: '))
i = 0
while(i < len(mass)):
    if(mass[i] >= start and mass[i] <= end):
        print(i, "(", mass[i], ")")
    i += 1