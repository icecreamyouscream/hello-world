# Числовая угадайка

import random


def is_valid(answer):  # функция, проверяющая число ли вводится
    if answer.isdigit():
        return 1 <= int(answer) <= right_value


def agreement(agree):  # функция проверки ввода Да/Нет
    return agree != 'Нет' and agree != 'Да'


print('Добро пожаловать в числовую угадайку!')
print('Хотите сыграть? Введите "Да" или "Нет"')
agree = input()
while agreement(agree):  # пока вводится неверное значение
    print('Необходимо ввести слова "Да" или "Нет" с заглавной буквы')
    agree = input()
if agree == 'Нет':
    print('Ничего страшного, просто вам это не интересно :)')
while agree == 'Да':
    print('До какого числа вы хотите угадывать?')
    right_value = int(input())  # правый предел рандомного числа
    n = random.randint(1, right_value)  # задается рандомное число от 1 до введенного игроком правого предела
    print('Тогда приступим! Введите число:')
    answer = input()  # считывается введенный ответ
    counter = 0  # счетчик попыток
    while is_valid(answer) is False:  # пока вводятся неверные значения
        print('А может быть все-таки введем целое число от 1 до ', right_value, '?', sep='')
        answer = input()  # считывается новый ответ
    while is_valid(answer):  # пока введено верное значение
        if int(answer) > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1  # счетчик попыток +1
            answer = input()  # считывается новый ответ
        elif int(answer) < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1  # счетчик попыток +1
            answer = input()  # считывается новый ответ
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
