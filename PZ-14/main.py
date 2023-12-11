import re


with open('hotline.txt', 'r', encoding='utf-8') as file:
    text = file.read()

count_changes = len(re.findall('«Горячая линия»', text))
text = re.sub('«Горячая линия»', '«Горячая линия министерства образования Ростовской области»', text)

print(f'Было сделано изменений: {count_changes}')
print('Новый текст\n\n',text, sep='')

end_03_count = 0
end_03_numbers = []
end_50_count = 0
end_50_numbers = []

for number in re.findall('\d{10,}', text):
    if number[-2:] == '03':
        end_03_count += 1
        end_03_numbers.append(number)
    elif number[-2:] == '50':
        end_50_count += 1
        end_50_numbers.append(number)
        
print(f'Количество номеров заканичивающихся на 03: {end_03_count}\n\
Вот эти номера {end_03_numbers}')

print(f'Количество номеров заканичивающихся на 50: {end_50_count}\n\
Вот эти номера {end_50_numbers}')

print('\n\n')
ege_numbers = []
for line in text.split('\n'):
    if re.findall('ЕГЭ|ГИА', line):
        ege_numbers.append(re.findall('\d{10,}', line)[0])
        
print(f'Номера телефонов связанные с ЕГЭ/ГИА: {ege_numbers}')