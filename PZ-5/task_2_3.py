
def count_digits(x):
    if type(x)  != int:
        raise ValueError(f'Число {x} не целое или не является числом. Проверьте вводимые типы данных')
    sum_digits = 0
    for digit in str(x):
        sum_digits += 1
    return sum_digits

#print(count_digits('koshka')) # Число koshka не целое или не является числом. Проверьте вводимые типы данных

print(count_digits(281234))