def max2(max,min): 
    if max > min: return max 
    return min 

def max3(a,b,c): 
    return max2(a, max2(b,c)) 

a,b,c = int(input('Введи первое число: ')), int(input('Введи второе число: ')), int(input('Введи третье число: ')) 

print('Максимальное число: ',max3(a,b,c))



def countInt(k): 
    t = 0 
    while k > 0: 
        k //= 10 
        t += 1
    return t 

Int_Nuber = input("Введи целое число: ") 
while type(Int_Nuber) != int: # обработка исключений 
    try: 
        Int_Nuber = int(Int_Nuber) 
    except ValueError: 
        print("Неправильно ввели!") 
        Int_Nuber = input("Введите целое число: ") 
        
print('Количество цифр в цисле: ', countInt(Int_Nuber))
    
    
def search_figure(k): 
    d = 10 
    while d != 100: 
        a, b = divmod(d, 10) 
        if (a == k) or (b == k): 
                print(d, -d) 
        d += 1

figure = input("Введи целое число от 0 до +- 9: ") 
while type(figure) != int: # обработка исключений 
    try: 
        figure = int(figure) 
    except ValueError: 
        print("Неправильно ввели!") 
        figure = input("Введите целое число: ") 

search_figure(figure)