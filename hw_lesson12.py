# 1
# Реализовать декоратор ЧЕРЕЗ КЛАСС!, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}
# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров

from functools import wraps
from typing import Callable
from datetime import datetime


# def decorate_add(func: Callable) -> Callable:
#
#     @wraps(func)
#     def inner(*args, **kwargs) -> tuple[tuple, dict]:
#         if not args and not kwargs:
#             print(f'Функция add вызвана в {datetime.now()} без параметров')
#         elif args and not kwargs:
#             print(f'Функция add вызвана в {datetime.now()} c позиционными параметрами {args}')
#         elif not args and kwargs:
#             print(f'Функция add вызвана в {datetime.now()} c именованными параметрами {kwargs}')
#         elif args and kwargs:
#             print(f'Функция add вызвана в {datetime.now()} c позиционными параметрами {args} и с именнованными парметрами {kwargs}')
#         return args, kwargs
#     return inner


class decorate_add:

    def __init__(self, func: Callable) -> Callable:
        self.func = func

    def __call__(self, *args, **kwargs):

        if not args and not kwargs:
            print(f'Функция add вызвана в {datetime.now()} без параметров')
        elif args and not kwargs:
            print(f'Функция add вызвана в {datetime.now()} c позиционными параметрами {args}')
        elif not args and kwargs:
            print(f'Функция add вызвана в {datetime.now()} c именованными параметрами {kwargs}')
        elif args and kwargs:
            print(f'Функция add вызвана в {datetime.now()} c позиционными параметрами {args} и с именнованными парметрами {kwargs}')
        return args, kwargs



@decorate_add
def add(*args, **kwargs):
    return args, kwargs



#add = decorate_add(add)
print(add())
print(add(1,3))
print(add(a=1, b=3))
print(add(1, b=3))



    # 2 (из ДЗ номер 5)
    # Написать функцию, которая принимает целое число n и выводит числа от 0 до n.
    # Если число является четным, вывести квадрат числа, вместо числа.
    # Если число делится на 7 и на 4 одновременно, процесс останавливается.
    # Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.