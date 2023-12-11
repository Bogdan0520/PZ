array = list(map(int, input().split()))

array2 = []

for i in range(len(array) - 1):
    array2.append(array[-1] * array[i])
    
print(array2)


# 1 2 3 4 5; [5, 10, 15, 20]
# 5 6 8 9 -3; [-15, -18, -24, -27]