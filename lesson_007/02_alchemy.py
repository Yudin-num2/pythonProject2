# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код


class Water:

    def __str__(self):
        return 'Я вода'

    def __add__(self, other):
        return Alchemy(item1=self, item2=other)


class Air:

    def __str__(self):
        return 'Я воздух'

    def __add__(self, other):
        return Alchemy(item1=self, item2=other)


class Alchemy:

    def __init__(self, item1, item2):
        self.item = item1
        self.other = item2

    def __str__(self):
        return 'Результат сложения: ', str(self.item + self.other)

    # def __add__(self, other):
    #     new_item = Alchemy
    #     new_tem = self.item + other.item
    #     return new_item


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым

water = Water()
air = Air()
new_item = water + air
print(new_item)
