def count_digits(x):
    sum_digits = 0
    while x > 0:
      sum_digits += x%10
      x//=10
    return sum_digits
a,b = int(input("Введите первое число: ")),int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
a1 = count_digits(a)
b1 = count_digits(b)
c1 = count_digits(c)
n = max(a1,b1,c1)
if n == a1:
  print("наибольшая сумма: ",n, " у числа " ,a)
if n == b1:
  print("наибольшая сумма: ",n, " у числа " ,b)
if n == c1:
  print("наибольшая сумма: ",n, " у числа " ,c)



print(max_sum_digits(000000,1000,2))
