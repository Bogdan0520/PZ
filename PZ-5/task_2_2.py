def rectangle_parameters(a,b):
    return 2*(a+b), a*b

a = int(input("Введите сторону a: "))
b = int(input("Введите сторону b: "))
per,sqw=rectangle_parameters(a, b)
print('Периметр прямоугольника: ', per,'\nЕго площадь: ', sqw)
