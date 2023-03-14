class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()

        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            None


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()

        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            None


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Vapor()

        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            None


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()

        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            None


class Storm:

    def __str__(self):
        return 'Шторм'


class Vapor:

    def __str__(self):
        return 'Пар'


class Dirt:

    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Brick()
        else:
            None


class Lightning:

    def __str__(self):
        return 'Молния'


class Dust:

    def __str__(self):
        return 'Пыль'


class Lava:

    def __str__(self):
        return 'Лава'


class Brick:

    def __str__(self):
        return 'Кирпич'


# def inpt():
#     word1 = input('Введите элемент 1: ')
#     word2 = input('Введите элемент 2: ')
#     if word1 == 'air' or word2 == 'air':
#         return Air()
#     elif word1 == 'earth' or word2 == 'earth':
#         return Earth()
#     elif word1 == 'fire' or word2 == 'fire':
#         return Fire()
#     elif word1 == 'water' or word2 == 'water':
#         return Water()

air = Air()
earth = Earth()
fire = Fire()
water = Water()

print(water + air)