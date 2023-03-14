from random import randint



class House:

    def __init__(self):
        self.money = 100
        self.meal = 50
        self.dirt = 0
        self.cat_meal = 30
        self.child_meal = 30

    def __str__(self):
        return 'В доме еды {}, денег {}, грязи {}, кошачьей еды {}'.format(
            self.meal, self.money, self.dirt, self.cat_meal)


class Man:

    def __init__(self, name):
        self.house = House()
        self.name = name
        self.fullness_man = 30
        self.fullness_woman = 30
        self.happiness_man = 100
        self.happiness_woman = 100

    def __str__(self):
        return

    def shopping(self):
        self.house.meal += 80
        self.house.money -= 170
        self.fullness_woman -= 10
        self.house.cat_meal += 40
        self.house.child_meal += 50
        return print('{} сходила в магазин'.format(self.name))

    def work(self):
        self.happiness_man -= 20
        self.fullness_man -= 10
        self.house.money += 150
        return print('{} сходил на работу'.format(self.name))

    def gaming(self):
        self.fullness_man -= 10
        self.happiness_man += 10
        return print('{} поиграл в WoT'.format(self.name))

    def buy_fur_coat(self):
        self.house.money -= 350
        self.happiness_woman += 60
        return print('{} купила шубу'.format(self.name))

    def clean_house(self):
        if self.house.dirt > 0:
            self.house.dirt -= randint(20, 50)
            self.fullness_woman -= 10
            return print('{} прибралась'.format(self.name))
        else:
            return print('{} отдыхает, в доме чисто'.format(self.name))

    def watch_TV(self):
        # self.happiness_woman += 10
        self.fullness_woman -= 10
        return print('{} смотрела телевизор весь день'.format(self.name))


class Husband(Man):

    def __init__(self, name, house):
        super().__init__(name=name)
        self.house = house

    def __str__(self):
        return 'Я {}, сытость {}, счастье {}'.format(self.name, self.fullness_man, self.happiness_man)

    def act(self):
        self.house.dirt += 5
        if self.fullness_man < 10 or self.happiness_man < 10:
            return print('{} умер...'.format(self.name))
        if self.house.dirt >= 90:
            self.happiness_man -= 10
        dice = randint(1, 6)
        if self.fullness_man < 20:
            self.eat()
        elif self.house.money < 50 or self.happiness_woman < 30:
            self.work()
        elif self.happiness_man < 20:
            self.gaming()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.petting_cat()
        else:
            self.gaming()

    def eat(self):
        self.fullness_man += 20
        self.house.meal -= 20
        return print('{} поел'.format(self.name))

    def petting_cat(self):
        self.happiness_man += 5
        return print('{} гладит кота'.format(self.name))


class Wife(Man):

    def __init__(self, name, house):
        super().__init__(name=name)
        self.house = house

    def __str__(self):
        return 'Я {}, сытость {}, счастье {}'.format(self.name, self.fullness_woman, self.happiness_woman)

    def act(self):
        if self.fullness_woman < 10 or self.happiness_woman < 10:
            return print('{} умерла...'.format(self.name))
        if self.house.dirt >= 90:
            self.happiness_woman -= 10
            self.clean_house()

        dice = randint(1, 6)
        if self.fullness_woman < 20:
            self.eat()
        elif self.house.meal <= 10 or self.house.cat_meal <= 10:
            self.shopping()
        elif self.house.money > 450 and dice == 1:
            self.buy_fur_coat()
        elif dice == 2:
            self.petting_cat()
        else:
            self.clean_house() if self.house.dirt > 50 else print('{} отдыхает'.format(self.name))

    def eat(self):
        self.fullness_woman += 20
        self.house.meal -= 20

        return print('{} поела'.format(self.name))

    def petting_cat(self):
        self.happiness_woman += 5
        return print('{} гладит кота'.format(self.name))


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30

    def __str__(self):
        return 'Я {}, сытость {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness < 5:
            return print('{} умер...'.format(self.name))
        dice = randint(1, 4)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.tear_up_the_wallpaper()
        else:
            self.sleep()

    def eat(self):
        self.fullness += 10
        self.house.cat_meal -= 10
        return print('{} поела'.format(self.name))

    def sleep(self):
        self.fullness -= 5
        return print('{} поспала'.format(self.name))

    def tear_up_the_wallpaper(self):
        self.house.dirt += 5
        return print('{} дерёт обои, падла'.format(self.name))


class Child:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30

    def __str__(self):
        return 'Я {}, сытость {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            return print('{} умер...'.format(self.name))
        dice = randint(1, 4)
        if self.fullness <= 10:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        _ = randint(5, 10)
        self.fullness += _
        self.house.child_meal -= _
        return print('{} поел'.format(self.name))

    def sleep(self):
        self.fullness -= 10
        return print('{} поспал'.format(self.name))

home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
child = Child(name='Кирилл', house=home)
murka = Cat(name='Мурка', house=home)

for day in range(1, 366):
    print('================== День {} =================='.format(day))

    serge.act()
    masha.act()
    child.act()
    murka.act()
    print(serge)
    print(masha)
    print(child)
    print(murka)
    print(home)


# TODO добавить несколько котов