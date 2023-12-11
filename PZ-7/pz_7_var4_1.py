
'''
Дано целое число N (1 < N < 26). Вывести N первых прописных (то есть заглавных) букв латинского алфавита.
'''

N = int(input())

for i in range(65, 65 + N):
    print(chr(i), end=' ')
    
    
    
# N = 4; A B C D 
# N = 26; A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 