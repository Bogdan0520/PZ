__all__ = ['triangle_perimeter', 'triangle_area']


a = 7
b = 2
c = 8

def triangle_perimeter(a=a,b=b,c=c):
    return a + b + c

def triangle_area(a=a,b=b,c=c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5