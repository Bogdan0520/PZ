'''
Дан словарь с четным количеством элементов. Найти суммы значений элементов первой и 
второй половин с использованием функции. Результаты вывести на экран.
'''


d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def dict_sum(d: dict):
    sum1 = 0
    sum2 = 0
    N = len(d)
    for i, (key, value) in enumerate(d.items()):
        if i < N // 2:
            sum1 += value
        else:
            sum2 += value
            
    return sum1, sum2
    
print(dict_sum(d1)) # (3, 7)
print(dict_sum(d2)) # (50, 150)
