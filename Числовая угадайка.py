# Числовая угадайка

import random

print('Добро пожаловать в числовую угадайку!')


def max_range():
    print('До какого числа вы хотите угадывать?')
    while True:
        max_value = input()
        if not max_value.isdigit() or int(max_value) < 2:
            print('Необходимо ввести целое число больше 1.')
            continue
        print(f'Отлично! Отгадываем от 1 до {max_value}!')
        return int(max_value)


def agreement(agree):
        if agree.lower() == 'да':
            return True
        elif agree.lower() == 'нет':
            return False
        else:
            return None


def valid_number():
    while True:
        num = input(f'Введите число от 1 до {q}:\n')
        if not num.isdigit() or not 1 <= int(num) <= q:
            print(f'А может быть все-таки введем целое число от 1 до {q}?\n')
            continue
        return int(num)


def game():
    x, counter = 0, 0
    while x != n:
        x = valid_number()
        if x < n:
            counter += 1
            print('Вы ввели число меньше загаданного, попробуйте еще разок.')
            continue
        elif x > n:
            counter += 1
            print('Вы ввели число больше загаданного, попробуйте еще разок.')
            continue
    print(f'Поздравляем! Вы угадали загаданное число с {counter} попыток!')


print('Хотите сыграть? Введите "Да" или "Нет":')
agree = input()
while agreement(agree) is None:
    agree = input('Необходимо ввести "Да" или "Нет".\n')
if agreement(agree) is False:
    print('Ничего страшного, вы просто случайно здесь оказались :)')
if agreement(agree):
    print('Хорошо, тогда начнем!')
    q = max_range()
    n = random.randint(1, q)
    while True:
        game()
        print('Хотите сыграть еще разок? Введите "Да" или "Нет":')
        agree = input()
        while agreement(agree) is None:
            agree = input('Необходимо ввести "Да" или "Нет".\n')
        if agreement(agree) is False:
            print('Спасибо, что играли в числовую угадайку! Всего хорошего :)')
            break
        if agreement(agree):
            print('Отлично! Тогда выбирайте новое число:')
            q = max_range()
            n = random.randint(1, q)
            continu
