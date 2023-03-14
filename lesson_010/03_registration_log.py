# -*- coding: utf-8 -*-
from pprint import pprint


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


file_adress = 'registrations.txt'
good_log_file = 'registrations_good_log.txt'
bad_log_file = 'registrations_bad_log.txt'
good_log = []
bad_log = []


def do(line):
    global good_log
    global bad_log
    # print(f'Текущая строка: {line}')
    operand_1, operand_2, operand_3 = line.split(' ')
    operand_3 = int(operand_3[:-1])
    if operand_1.isalpha():
        if '@' and '.' in operand_2:
            if 10 <= operand_3 <= 99:
                good_log.append(line)
            else:
                bad_log.append(line)
        else:
            bad_log.append(line)
            raise NotEmailError
    else:
        bad_log.append(line)
        raise NotNameError

    return good_log, bad_log


with open(file_adress, 'r', encoding='utf8') as file:
    for line in file:
        try:
            do(line)
        except ValueError as val:
            if 'unpack' in val.args:
                print(f'Неправильно указан возраст в строке: {line}', end='')
            else:
                print(f'Проверьте данные пользователя в строке: {line}', end='')
        except NotNameError as nnerr:
            print(f'Имя пользователя содержит не только буквы в строке: {line}', end='')
        except NotEmailError as neerr:
            print(f'Неправильно введён email в строке: {line}', end='')

with open(good_log_file, mode='w', encoding='utf8') as good_file:
    good_file.write(str(good_log))

with open(bad_log_file, mode='w', encoding='utf8') as bad_file:
    bad_file.write(str(bad_log))
