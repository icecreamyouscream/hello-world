# MyProfile app
def separator():
    print('------------------------------------------')


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, info_parameter, ind_parameter, address_parameter):
    separator()
    print('Имя:     ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст: ', age_parameter, years_parameter)
    print('Телефон: ', phone_parameter)
    print('E-mail:  ', email_parameter)
    print('Индекс:  ', ind_parameter)
    print('Адрес:   ', *address_parameter)
    if info:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # главное меню
    separator()
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        print('Завершение программы...')
        break

    if option == 1:
        # подменю 1: редактирование информации
        while True:
            separator()
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предприятии')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # ввод личных данных

                name = input('Введите имя: ')
                name = name.capitalize()

                while 1:
                    # возраст
                    age = input('Введите возраст: ')
                    if not age.isdigit() or int(age) < 0:
                        print('Необходимо вводить только циферные значения больше нуля!')
                        continue
                    elif age.isdigit() and int(age) > 0:
                        age = int(age)
                        break

                while 1:
                    # номер телефона
                    phone = input('Введите номер телефона без "+7": ')
                    if '+7' in phone:
                        print('Пожалуйста, введите номер телефона без кода!')
                        continue
                    elif len(phone) > 10 or len(phone) < 10:
                        print('Номер телефона без кода должен содержать 10 цифр!')
                        continue
                    elif phone.isdigit():
                        phone = '+7' + phone
                        break

                while 1:
                    # адрес электронной почты
                    email = input('Введите email: ')
                    if email.find('@') > email.find('.'):
                        print('Знак "@" должен находиться перед доменом!')
                        continue
                    elif '@' not in email and ('.ru' not in email or '.com' not in email or '.org' not in email):
                        print('Email должен содержать "@", а так же ".ru" или ".com", или ".org". Попробуйте еще раз!')
                        continue
                    else:
                        break

                while 1:
                    # индекс
                    index = input('Ведите почтовый индекс: ')
                    if index.isalnum():
                        new_index = ''
                        for char in index:
                            if char.isdigit():
                                new_index += char
                    break

                # почтовый адрес
                address = input('Введите почтовый адрес (без индекса): ').split()

                # дополнительная информация
                info = input('Введите дополнительную информацию: ')

            elif option2 == 2:
                # input company info

                while True:
                    # ОГРНИП
                    gos_reg_number = input('Введите ОГРНИП (15 цифр): ')
                    if not gos_reg_number.isdigit():
                        print('В ОГРНИП должны содержаться только цифры.')
                        continue
                    elif len(gos_reg_number) != 15:
                        print('В ОГРНИП должно быть 15 цифр.')
                        continue
                    elif gos_reg_number.isdigit() and len(gos_reg_number) == 15:
                        break

                while True:
                    # ИНН
                    nalog_number = input('Введите ИНН (12 цифр): ')
                    if not nalog_number.isdigit():
                        print('В ИНН должны содержаться только цифры.')
                        continue
                    elif len(nalog_number) != 12:
                        print('В ИНН должно быть 12 цифр.')
                        continue
                    elif nalog_number.isdigit() and len(nalog_number) == 12:
                        break

                while True:
                    # рассчетный счет
                    check_account = input('Введите свой расчетный счет (20 цифр): ')
                    if not check_account.isdigit():
                        print('В р/с должны содержаться только цифры.')
                        continue
                    elif len(check_account) != 20:
                        print('В р/с должно быть 20 цифр.')
                        continue
                    elif check_account.isdigit() and len(check_account) == 20:
                        break

                while True:
                    # наименование банка
                    bank = input('Введите наименование банка: ')
                    if not bank.isalnum():
                        print('Такого банка не существует.')
                        continue
                    elif bank.isalnum():
                        bank = bank.capitalize()
                        break

                while True:
                    # БИК
                    bik_number = input('Введите БИК Вашего банка (9 цифр): ')
                    if not bik_number.isdigit():
                        print('БИК должен содержать только цифры.')
                        continue
                    elif len(bik_number) != 9:
                        print('В БИК должно быть 9 цифр.')
                        continue
                    elif bik_number.isdigit() and len(bik_number) == 9:
                        break

                while True:
                    # корреспондентский счет
                    korr_account = input('Введите корреспондентский счет (20 цифр), если он есть. Если к/с нет - введите "-" или напишите "нет": ')
                    if korr_account == '-' or korr_account == 'нет':
                        break
                    if not korr_account.isdigit():
                        print('В к/с должны содержаться только цифры.')
                        continue
                    elif len(korr_account) != 20:
                        print('В к/с должно быть 20 цифр.')
                    elif korr_account.isdigit() and len(korr_account) == 20:
                        break
            else:
                print('Введите корректный пункт меню')

    elif option == 2:
        # submenu 2: print info
        while True:
            separator()
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))

            if option2 == 0:
                break

            if option2 == 1:
                general_info_user(name, age, phone, email, info, index, address)

            elif option2 == 2:
                general_info_user(name, age, phone, email, info, index, address)
                print()
                # вывод данных предприятия
                print('ОГРНИП:  ', gos_reg_number)
                print('ИНН:     ', nalog_number)
                print('Р/с:     ', check_account)
                print('Банк:    ', bank)
                print('БИК:     ', bik_number)
                print('К/с:     ', korr_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
