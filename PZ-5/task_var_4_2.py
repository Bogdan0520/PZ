def RectPS(x1,x2,y1,y2, P,S):
    a = abs(x1-x2)
    b = abs(y1-y2)
    P = 2*(a+b)
    S = a*b
    return P, S

P=0
S=0
P,S = RectPS(1,2,3,4,P,S)
print(f'Периметр прямоугольника: ',P ,'\n Его площадь: ',S )
P,S = RectPS(-1,-2,3,4,P,S)
print(f'Периметр прямоугольника: ',P ,'\n Его площадь: ',S )
P,S = RectPS(16.6,92,-38,44,P,S)
print(f'Периметр прямоугольника: ',P ,'\n Его площадь: ',S )
