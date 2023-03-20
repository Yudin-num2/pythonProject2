# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле
import os
from operator import itemgetter
from pprint import pprint
import time
from threading import Thread
def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class Volater:

    def __init__(self, path, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        self.path = path
        self.sorted_total_prices = []
        self.all_volatilitys = {}
        self.zero_volatility = {}
        self.max = None
        self.min = None

    @time_track
    def run(self):

        for dirname, dirpath, files in os.walk(self.path):
            for file in files:
                total_prices = []
                with open(os.path.join(dirname, file), mode='r', encoding='utf8') as f:
                    for line in f:
                        if 'PRICE' not in line:
                            price = float(line.split(',')[2])
                            total_prices.append(price)
                self.sorted_total_prices = sorted(total_prices)
                average_price = (self.sorted_total_prices[-1] + self.sorted_total_prices[0]) / 2
                volatility = round(((self.sorted_total_prices[-1] -
                                     self.sorted_total_prices[0]) / average_price) * 100, 3)
                if volatility == 0.0:
                    self.zero_volatility[file] = volatility
                else:
                    self.all_volatilitys[file] = volatility
                    self.max = sorted(self.all_volatilitys.items(), key=itemgetter(1))[-1:-4:-1]
                    self.min = sorted(self.all_volatilitys.items(), key=itemgetter(1))[0:3]
            print(f'Максимальная волатильность: \n {self.max}')
            print(f'Минимальная волатильность: \n {self.min}')
            print(f'Нулевая волатильность: \n {self.zero_volatility}')


volater = Volater(path=r'C:\Users\i.sysoev\PycharmProjects\pythonProject2\lesson_012\trades')
volater.run()
