# Даны три целых числа. Найти количество положительных чисел в исходном наборе.
a, b, c = input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ") 
while type(a) != int: # обработка исключений 
    try: a = int(a) 
    except ValueError: 
        print("Неправильно ввели!") 
        a = input("Введите первое число: ") 
        
while type(b) != int: # обработка исключений 
    try: b = int(b) 
    except ValueError: 
        print("Неправильно ввели!") 
        b = input("Введите второе число: ") 
        
while type(c) != int: # обработка исключений 
    try: c = int(c) 
    except ValueError: 
        print("Неправильно ввели!") 
        c = input("Введите третье число: ") 
    
k = 0 
if a > 0: k += 1    
if b > 0: k += 1 
if c > 0: k += 1 
print('Количество положительных чисел = ', k) 

