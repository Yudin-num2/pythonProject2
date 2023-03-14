from random import randint


results = {'bulls': 0, 'cows': 0}
i = 0
coincidences = 0
random_number = str(randint(1000, 9999))


def check_number(users_number):

    global results, i, coincidences

    print(random_number)
    for coincidences in range(0, 4):
        if random_number[coincidences] == users_number[coincidences]:
            results['bulls'] += 1
        elif random_number[coincidences] in users_number:
            results['cows'] += 1
        i += 1
    return print('Число быков: ', results['bulls'], 'Число коров: ', results['cows'])

def game_over():
    return results.values() == [4, 0]

# При запуске игры если вводить каждый раз одно и тоже число, количество быков постоянно растёт
# ИГРА НАЧИНАЕТСЯ
# Введите число : 1234
# 5238
# Число быков:  2
# Число коров:  0
# Введите число : 5234
# 5238
# Число быков:  5 Число коров:  0
# Введите число : 5235
# 5238
# Число быков:  8 Число коров:  0
# Введите число : 5285
# 5238
# Число быков:  10 Число коров:  1
# Введите число :




