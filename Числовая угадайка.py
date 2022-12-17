# Числовая угадайка

import random


def is_valid(answer):
    if answer.isdigit():
        return 1 <= int(answer) <= right_value


def agreement(agree):
    return agree != 'Нет' and agree != 'Да'


print('Добро пожаловать в числовую угадайку!')
print('Хотите сыграть? Введите "Да" или "Нет"')
agree = input()
while agreement(agree):
    print('Необходимо ввести слова "Да" или "Нет" с заглавной буквы')
    agree = input()
if agree == 'Нет':
    print('Ничего страшного, просто вам это не интересно :)')
while agree == 'Да':
    print('До какого числа вы хотите угадывать?')
    right_value = int(input())
    n = random.randint(1, right_value)
    print('Тогда приступим! Введите число:')
    answer = input()
    counter = 0
    while is_valid(answer) is not True:
        print('А может быть все-таки введем целое число от 1 до числа, которое вы сами назвали?')
        answer = input()
    while is_valid(answer) is True:
        if int(answer) > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
            answer = input()
        elif int(answer) < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
            answer = input()
        elif int(answer) == n:
            print('Вы угадали, поздравляем!')
            print('Попыток:', counter)
            break
    print('Хотите сыграть еще разок? Введите "Да" или "Нет":')
    agree = input()
    while agreement(agree):
        print('Необходимо ввести слова "Да" или "Нет" с большой буквы')
        agree = input()
    if agree == 'Нет':
        print('Спасибо, что играли в числовую угадайку!')
        break