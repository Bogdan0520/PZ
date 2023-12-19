a,b = int(input("Введите первое число: ")),int(input("Введите второе число: "))
c = max(a,b)
print("наибольшее число: ",c)
y = int(input("Введите третье число: "))
c = max(a,b,y)
print("наибольшее число: ",c)
b = int(input("Введите многоразрядное, целое число: "))
t = 0
while b>0:
  t += 1
  b//=10
print(t)
#Нахождение всех двузначных чисел, в которых есть заданная цифра
def digit(n,a):
  t= False
  while n>10:
    if n%10 == a:
      t=True
    n//=10
  return t

a = int(input("Введите цифру: "))
for n in range(10,100):
  if digit(n,a)==True:
    print(n)
