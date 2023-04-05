import random
# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.


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
for i in iter(first):
    item = iter(first)
    print(next(item))

print('==================================')


def generator_object(start_range: int, stop_range: int, start_number: int = None):
    while True:
        rezult = random.randint(start_range, stop_range)
        yield rezult

#second = generator_object(23, 100)
for i in range(10):
    print(next(generator_object(23, 100)))



