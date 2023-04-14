from typing import Iterator

my_list = ['a', 'b', 'c']

def enum_generator(my_list: list, start: int = 0) -> Iterator[tuple]:
    count = start
    for val in my_list:
        yield count, val
        count +=1

# tuple_result = enum_generator(my_list)
# print(next(tuple_result))
# print(next(tuple_result))
# print(next(tuple_result))
for value in enum_generator(my_list, 3):
    print(value)