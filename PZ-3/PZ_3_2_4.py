#Дано целое число. Если оно является положительным, то прибавить к нему 20, в противном случае вычесть из него 5.


a= input('Введите целое число')

while type(a)!= int:
    try:
        a = int(a)
    except:
        print('Неправильно ввели число a')
        a = input('Введите целое число')

if a > 0:
    print(a + 20)
else:
    print(a - 5)