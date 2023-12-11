try:
    arr = list(map(float, input().split()))
except:
    raise BaseException('Один из элементов массива не может быть сконвертирован в тип float')

N = len(arr)

min_num = 0
min_elem = arr[0]
max_num = 0
max_elem = arr[0]


for i in range(N):
    if arr[i] > max_elem:
        max_elem = arr[i]
        max_num = i
    if arr[i] < min_elem:
        min_elem = arr[i]
        min_num = i
      
i = min_num
j = max_num
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
print(arr) 
    
# 1 1 0 1 2 3 4 5 6 1 1 1; [1.0, 1.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 1.0, 1.0]
# 1 2 3 4 5; [5.0, 4.0, 3.0, 2.0, 1.0]
# 1 aa 34; BaseException: Один из элементов массива не может быть сконвертирован в тип float
    