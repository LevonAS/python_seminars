'''
Реализуйте алгоритм перемешивания списка
'''

import random

my_data = ['4', 'Море', 'done', '#4v@', '0.34']
# Для реализации есть готовая функция
random.shuffle(my_data)
print(my_data)

# Можно использовать случайный  ключ для сортировки
print(sorted(my_data, key=lambda i: random.random()))

# ['0.34', 'Море', '#4v@', 'done', '4']
# ['#4v@', '4', 'done', 'Море', '0.34']
