



def RectPS(x1,x2,y1,y2):
    for elem in [x1,x2,y1,y2]:
        if type(elem) not in (int, float):
            raise ValueError(f'{elem} не является вещественным числом')
    a = abs(x1-x2)
    b = abs(y1-y2)
    print(f'Периметр прямоугольника: {2*(a+b)}\n\
Его площадь: {a*b}')
    
#RectPS('banan',1,2,3) #ValueError: banan не является вещественным числом
# RectPS(4,'koshka',2,3) #ValueError: koshka не является вещественным числом

RectPS(1,2,3,4)
RectPS(-1,-2,3,4)
RectPS(16.6,92,-38,44)