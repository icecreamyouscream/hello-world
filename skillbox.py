number = int(input('Кол-во человек: '))
ppl_amt = []
for ppl in range(number):
    ppl_amt.append(ppl + 1)
count_num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый ', count_num, '-й человек', sep='')

print('\nТекущий круг людей:', ppl_amt)
copy_ppl_amt = ppl_amt.copy()
while True:
    print('Начало счета с номера', copy_ppl_amt[0])
    shift = count_num % len(copy_ppl_amt) - 1
    new_list = copy_ppl_amt[shift:]
    shift_part = copy_ppl_amt[:shift]
    new_list.extend(shift_part)
    print('Выбывает человек под номером', new_list[0])
    ppl_amt.remove(new_list[0])
    new_list.remove(new_list[0])
    copy_ppl_amt = new_list.copy()
    if len(ppl_amt) == 1:
        print('\nОстался человек под номером', ppl_amt[0])
        break
    print('\nТекущий круг людей:', ppl_amt)
