try:
    arr = list(map(float, input().split()))
except:
    raise BaseException('Один из элементов массива не может быть сконвертирован в тип float')

N = len(arr)

local_max = 0
for i in range(N - 1):
    if arr[i]> arr[i+1] and arr[i] > arr[i - 1]:
        local_max = i
if arr[-1] > arr[-2]:
    local_max = len(arr) - 1
        
print(local_max)

# 1 b 4; BaseException: Один из элементов массива не может быть сконвертирован в тип float
# 1 2 3 4 5; 4
# 0 23 6 3 2; 1
# 1 5 3 4 3; 3
# 5 4 3 2 1; 0