import random
# 2
# Добавить обработку исключений в следующие задания:
    # 3* (из ДЗ номер 3)
    # Написать мини-игру «Камень ножницы бумага с ботом», в которой пользователь должен выбрать либо камень,
    # либо ножницы, либо бумагу. Бот делает случайный выбор (случайное число).
    # Вывести результат если, например, игрок выбрал бумагу, а бот ножницы:
    # Бот выбрал ножницы, вы проиграли!
    # Подсказка: я не показывала, как в Pyhon получить случайное число, попробуйте найти это сами


class NotFoundError(Exception):
    pass


answers = ['Камень', 'Ножницы', 'Бумага']
while True:
    answer = input('Enter once answer (Камень или Ножницы или Бумага) ')
    try:
        if answer.title() not in answers:
            raise NotFoundError
    except NotFoundError:
        print('Вы ввели не допустимый ответ попробуйте еще раз')
        continue
    answer_bot = random.choice(answers)
    if answer.title() == answer_bot:
        print(f'Бот выбрал {answer_bot} и вы выбрали {answer}, ничья!')
    elif (answer.title() == 'Бумага' and answer_bot == 'Ножницы') or (answer.title() == 'Ножницы' and answer_bot == 'Камень')\
            or (answer.title() == 'Камень' and answer_bot == 'Бумага'):
        print((f'Бот выбрал {answer_bot}, вы проиграли!'))
    else:
        print((f'Бот выбрал {answer_bot}, вы победили!'))
    print('Хотите сыграть еще раз?')
    res =input('y/n:')
    try:
        if res != 'y' or res !='n':
            raise NotFoundError
    except NotFoundError:
        print('Вы ввели не допустимое значение попробуйте еще раз')
        print('Хотите сыграть еще раз?')
        res = input('y/n:')
    if res == 'n':
        print('Спасибо за игру. Удачного дня.')
        break
