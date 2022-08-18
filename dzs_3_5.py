'''
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов [Негафибоначчи].
Пример:
- для k = 8 список будет выглядеть так:
 [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

num = int(input('Введите число: '))

fib_1 = fib_3 = fib_4 = 1
fib_2 = -1
res = []

res.append(0)
res.append(fib_1)
res.append(fib_2)
for i in range(2, num):
    fib_1, fib_2 = fib_2, fib_1 - fib_2
    res.append(fib_2)

res.reverse()
res.append(fib_3)
res.append(fib_4)
for i in range(2, num):
    fib_3, fib_4 = fib_4, fib_3 + fib_4
    res.append(fib_4)

print(f"Для заданного числа {num},\n"
      f"список чисел Фибоначчи выглядит = {res}")

# Введите число: 8
# Для заданного числа 8,
# список чисел Фибоначчи выглядит = [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Как-то так
