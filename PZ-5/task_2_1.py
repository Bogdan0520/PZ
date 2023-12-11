


def count_digits(x):
    if type(x)  != int:
        raise ValueError(f'Число {x} не целое или не является числом. Проверьте вводимые типы данных')
    sum_digits = 0
    for digit in str(x):
        sum_digits += int(digit)
    return sum_digits

def max_sum_digits(a, b, c):
    max_result = 0
    max_elem = a
    for index, elem in enumerate([a,b,c]):
        if count_digits(elem) > max_result:
            max_result = count_digits(elem)
            max_elem = elem
    return max_elem
    
    
    

#print(max_sum_digits(1,2,'koshka')) #Число koshka не целое или не является числом. Проверьте вводимые типы данных


print(max_sum_digits(123,245,999))

print(max_sum_digits(000000,1000,2))