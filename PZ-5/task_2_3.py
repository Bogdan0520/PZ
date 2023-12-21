def count_digits(x):
  t = 0
  while x>0:
    t += 1
    x//=10
  return t
a = int(input("введите число "))
k = count_digits(a)
print(k)
