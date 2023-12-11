

def rectangle_parameters(a,b):
    if type(a) not in (int, float):
        raise ValueError(f'{a} не является вещественным числом')
    if type(b) not in (int, float):
        raise ValueError(f'{b} не является вещественным числом')
    
    print(f'Периметр прямоугольника: {2*(a+b)}\n\
Его площадь: {a*b}')
    
    
#rectangle_parameters('banan', 4) #banan не является вещественным числом
#rectangle_parameters(5, 'koshka') # koshka не является вещественным числом

rectangle_parameters(1,2) 
rectangle_parameters(14.3, 5)