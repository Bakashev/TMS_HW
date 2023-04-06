import random
# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.
# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.


class IterableObject:

    def __init__(self, start_range: int, stop_range: int ):
        self.stop_number = random.randint(start_range, stop_range)
        self.start_range = start_range
        self.stop_range = stop_range

    def __iter__(self):
        return self

    def __next__(self):
        rezult = random.randint(self.start_range, self.stop_range)
        if rezult == self.stop_number:
            print(f'Случайное число {rezult} = стоп числу {self.stop_number}')
            raise StopIteration

        return rezult


first = IterableObject(19, 30)
print(f'стоп число {first.stop_number}')
for i in first:
    #item = iter(first)
    print(i)

print('==================================')


def generator_object(start_range: int, stop_range: int, stop_number:int = None):
    my_rezult = 0
    while my_rezult != stop_number:
        my_rezult = random.randint(start_range, stop_range)
        print(f' стоп число {stop_number}, результат {my_rezult}')
        yield my_rezult


second = generator_object(23, 100, 24)
for i in second:
    print(i)



