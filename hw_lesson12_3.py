# 2 (из ДЗ номер 5)
# Написать функцию, которая принимает целое число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.


def int_number(number: int) -> int:
    for i in range(number):
        if i == 0 or i % 2 != 0:
            print(i,end=' ')
        if i % 2 == 0 and i != 0:
            print(i ** 2, end=' ')
        if i % 7 == 0 and i % 4 == 0 and i != 0:
            break


try:
    num = int(input('Введите целое число: '))
    int_number(num)
except ValueError:
    print('Введено недопустимое значение')


