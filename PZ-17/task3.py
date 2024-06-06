import os

print('''Пункт 1. 
      
Перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена 
вложенных подкаталогов выводить не нужно.

Результат:''')
print(os.listdir('../PZ-11'))

print('''
Пунтк 2. 
Перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере 
файлов в папке test.      
      ''')
if not os.path.exists('../test/test1'):
    os.mkdir('../test/test1')

with open('../PZ-6/Untitled - Frame 4.jpg', 'rb') as file1:
    with open('../test/Untitled - Frame 4.jpg', 'wb') as file2:
        file2.write(file1.read())
        
with open('../PZ-6/var4_2.py', 'rb') as file1:
    with open('../test/var4_2.py', 'wb') as file2:
        file2.write(file1.read())
        
with open('../PZ-7/pz_7_var4_1.py', 'rb') as file1:
    with open('../test/test1/test.txt', 'wb') as file2:
        file2.write(file1.read())
        

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                total_size += os.path.getsize(filepath)
    return total_size


print(f'Размер файлов в папке test: {get_directory_size("../test")}\n\n')


print('''Пункт 3. 
      
Перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в 
консоль. Использовать функцию basename  (os.path.basename()).     

''')


shortest_file = min(os.listdir('../PZ-11'), key=len)
print(f'Файл с самым коротким названием: {os.path.basename(shortest_file)}')

print('''Пункт 4.
      
Перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в 
привязанной к нему программе. Использовать функцию os.startfile().
''')

os.chdir('../PZ-2')
os.startfile('otchet.pdf')
print('Файл успешно запущен')

print('''Пункт 5.
      
Удалить файл test.txt
''')
os.chdir('../test/test1')
print(os.listdir())
os.remove('test.txt')
print(os.listdir())


# Пункт 1.

# Перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.

# Результат:
# ['new_file.txt', 'otchet_pz11.docx', 'otchet_pz11.pdf', 'otchet_pz11_v1.pdf',
#     'pz_11_var4_1.py', 'pz_11_var4_2.py', 'result.txt', 'some.txt', 'text18-4.txt']

# Пунтк 2.
# Перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.

# Размер файлов в папке test: 420240


# Пункт 3.

# Перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename(os.path.basename()).


# Файл с самым коротким названием: some.txt
# Пункт 4.

# Перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему программе. Использовать функцию os.startfile().

# Файл успешно запущен
# Пункт 5.

# Удалить файл test.txt

# ['test.txt', 'var4_1.py']
# ['var4_1.py']
