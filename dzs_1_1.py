"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
 и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
"""

user_input = input('Введите число дня недели: ')

try:
    if user_input.isdigit():
        if 6 <= int(user_input) <= 7:
            print("да")
        elif 0 < int(user_input) < 6:
            print("нет")
        else:
            print("введено неправильное число")
    else:
        raise ValueError(f"'{user_input}' не является числом")
except ValueError as e:
    print(e)


# Введите число дня недели: 3
# нет

# Введите число дня недели: 6
# да
