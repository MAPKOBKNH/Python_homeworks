# Вариант с преобразованием любого введенного числа в положительное целое
# при этом происходит округление !!
n = float(input('enter your number: '))  # ввод
n = int(float('{:.0f}'.format(n)))  # преобразование в целое с округлением
print('INT type number (rounded) is: ', (n))
if n < 0:
    n *= -1  # вовзвращение к положительному числу (исключение ошибки ввода)
i = 0  # переменная, принимающая при сравнении значение наибольшего числа
while n > 0:
    num = n % 10  # берем последнюю цифру
    n = n // 10  # убираем последнюю взятую из числа
    if num == 9:  # число не может быть больше 9 (проверка и прерывание)
        i = num
        break
    elif i <= num:  # сравнение
        i = num  # присвоение максимума контрольной ячейке
print('max number is: ', (i))
