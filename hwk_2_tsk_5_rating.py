"""Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

"""

my_list = [7, 5, 3, 3, 2]

while True:
    el = input('Enter number (Q- quit): ')  # ввод числа и задание маркера
    mark = False

    if el == "Q":  # условие выхода и печати
        print(my_list)
        break
    el = int(el)

    for i in range(len(my_list)):
        if el > my_list[i]:
            my_list.insert(i, el)
            mark = True
            break  # для предотвращения задвоения
    if not mark:
        my_list.append(el)
