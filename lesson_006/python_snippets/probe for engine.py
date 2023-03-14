from random import randint

random_number = str(randint(1000, 9999))
print(random_number)
users_number = input('Введите число: ')
results = {'bulls': 0, 'cows': 0}
i = 0
coincidences = 0


def probe():
    global random_number, users_number, results, i, coincidences

    for coincidences in range(0, 4):

        if random_number[coincidences] == users_number[coincidences]:
            results['bulls'] += 1
        elif random_number[coincidences] in users_number:
            results['cows'] += 1
        i += 1
    print(results)


probe()

