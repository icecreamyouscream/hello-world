def separation():
    print('------------------------------------------')


def option():
    while True:
        option = input('Введите номер пункта меню: ')
        if not option.isalnum() or option < '0' or option > '2':
            print('Необходимо ввести 0, 1 или 2!')
            continue
        elif option.isalnum():
            option = int(option)
        return option


def personal_info_out():
    print('Имя:', personal_name())
    print('Возраст:', personal_age())
    print('Телефон:', personal_phone())
    print('E-mail: ', personal_email())
    if 1 == 1:
        print('Дополнительная информация:', extra_info())


def company_info_out():
    print('ОГРНИП:', gos_number())
    print('ИНН:', inn())
    print('Рассчетный счет:', check_acc())
    print('Наименование банка:', bank_name())
    print('БИК банка:', bik())
    print('Корреспондентский счет:', korr_acc())


def personal_name():
    while 1:
        name = input('Введите имя: ')
        if not name.isalpha():
            print('В имени должны содержаться только буквы!')
            continue
        elif name.isalpha():
            return name.capitalize()


def personal_age():
    while 1:
        age = input('Введите возраст: ')
        if not age.isdigit() or int(age) < 0:
            print('Необходимо вводить только циферные значения больше нуля!')
            continue
        elif age.isdigit() and int(age) > 0:
            return int(age)


def personal_phone():
    while 1:
        phone = input('Введите номер телефона без "+7": ')
        if '+7' in phone:
            print('Пожалуйста, введите номер телефона без кода!')
            continue
        elif len(phone) > 10 or len(phone) < 10:
            print('Номер телефона без кода должен содержать 10 цифр!')
            continue
        elif phone.isdigit():
            phone = '+7' + phone
            return phone


def personal_email():
    while 1:
        email = input('Введите email: ')
        if email.find('@') > email.find('.'):
            print('Знак "@" должен находиться перед доменом!')
            continue
        elif '@' not in email and ('.ru' not in email or '.com' not in email or '.org' not in email):
            print('Email должен содержать "@", а так же ".ru" или ".com", или ".org". Попробуйте еще раз!')
            continue
        else:
            return email


def gos_number():
    while True:
        gos_reg_number = input('Введите ОГРНИП (15 цифр): ')
        if not gos_reg_number.isdigit():
            print('В ОГРНИП должны содержаться только цифры.')
            continue
        elif len(gos_reg_number) != 15:
            print('В ОГРНИП должно быть 15 цифр.')
            continue
        elif gos_reg_number.isdigit() and len(gos_reg_number) == 15:
            return gos_reg_number


def inn():
    while True:
        nalog_number = input('Введите ИНН (12 цифр): ')
        if not nalog_number.isdigit():
            print('В ИНН должны содержаться только цифры.')
            continue
        elif len(nalog_number) != 12:
            print('В ИНН должно быть 12 цифр.')
            continue
        elif nalog_number.isdigit() and len(nalog_number) == 12:
            return nalog_number


def check_acc():
    while True:
        check_account = input('Введите свой расчетный счет (20 цифр): ')
        if not check_account.isdigit():
            print('В р/с должны содержаться только цифры.')
            continue
        elif len(check_account) != 20:
            print('В р/с должно быть 20 цифр.')
            continue
        elif check_account.isdigit() and len(check_account) == 20:
            return check_account


def bank_name():
    while True:
        bank = input('Введите наименование банка: ')
        if not bank.isalnum():
            print('Такого банка не существует.')
            continue
        elif bank.isalnum():
            bank.capitalize()
            return bank


def bik():
    while True:
        bik_number = input('Введите БИК Вашего банка (9 цифр): ')
        if not bik_number.isdigit():
            print('БИК должен содержать только цифры.')
            continue
        elif len(bik_number) != 9:
            print('В БИК должно быть 9 цифр.')
            continue
        elif bik_number.isdigit() and len(bik_number) == 9:
            return bik_number


def korr_acc():
    while True:
        korr_account = input('Введите корреспондентский счет (20 цифр), если он есть. Если к/с нет - введите "-" или напишите "нет": ')
        if korr_account == '-' or korr_account == 'нет':
            break
        if not korr_account.isdigit():
            print('В к/с должны содержаться только цифры.')
            continue
        elif len(korr_account) != 20:
            print('В к/с должно быть 20 цифр.')
        elif korr_account.isdigit() and len(korr_account) == 20:
            return korr_account


def extra_info():
    info = input('Дополнительная информация: ')
    if len(info) > 0:
        return info
    else:
        return None


def sub_edit_info():
    # submenu 1: edit info
    print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
    print('1 - Личная информация')
    print('2 - Информация о предпринимателе')
    print('0 - Назад')

    if option() == 1:
        personal_name()
        personal_age()
        personal_phone()
        personal_email()
        extra_info()
    elif option() == 2:
        gos_number()
        inn()
        check_acc()
        bank_name()
        bik()
        korr_acc()
    elif option() == 0:
        main_menu()


def main_menu():
    while True:
        # main menu
        separation()
        print('ГЛАВНОЕ МЕНЮ')
        print('1 - Ввести или обновить информацию')
        print('2 - Вывести информацию')
        print('0 - Завершить работу')

        if option() == 1:
            sub_edit_info()
        elif option() == 2:
            personal_info_out()

        elif option() == 0:
            print('Завершение работы...')


main_menu()
