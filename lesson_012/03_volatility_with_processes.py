# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

# TODO тут ваш код в многопроцессном стиле
import os
from operator import itemgetter
import time
from multiprocessing import Process, Pipe, Queue


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class Volater(Process):

    def __init__(self, f, connection, all_volatilitys, zero, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = f
        self.sorted_total_prices = []
        self.all_volatilitys = all_volatilitys
        self.zero_volatility = zero
        self.connection = connection


    def run(self):

        with open(file=os.path.join('trades', self.f), mode='r', encoding='utf8') as file:

            total_prices = []
            for line in file:
                if 'PRICE' not in line:
                    price = float(line.split(',')[2])
                    total_prices.append(price)
        self.sorted_total_prices = sorted(total_prices)
        average_price = (self.sorted_total_prices[-1] + self.sorted_total_prices[0]) / 2
        volatility = round(((self.sorted_total_prices[-1] -
                             self.sorted_total_prices[0]) / average_price) * 100, 3)
        if volatility == 0.0:
            self.zero_volatility[self.f] = volatility
            self.connection.send(self.zero_volatility)
            self.connection.close()
        elif volatility:
            self.all_volatilitys[self.f] = volatility
            self.connection.send(self.all_volatilitys)
            self.connection.close()



all_volatility = {}
zero = {}
path_to_directory = r'C:\Users\i.sysoev\PycharmProjects\pythonProject\lesson_012\trades'
all_files = []
volaters, pipes = [], []
@time_track
def main():

    for dirname, dirpath, files in os.walk(path_to_directory):
        for file in files:
            all_files.append(file)

    for f in all_files:
        parent_connection, child_connection = Pipe()

        volater = Volater(f=f, connection=child_connection, all_volatilitys=all_volatility, zero=zero)
        volaters.append(volater)
        pipes.append(parent_connection)

    for volater in volaters:
        volater.start()
    for connection in pipes:
        all_volatilits = connection.recv()
        max_volatilitys = sorted(all_volatilits.items(), key=itemgetter(1))[-1:-4:-1]
        min_volatilitys = sorted(all_volatilits.items(), key=itemgetter(1))[0:3]
        print(max_volatilitys)


    # print(f'Максимальная волатильность: \n {max_volatilitys}')
    # print(f'Минимальная волатильность: \n {min_volatilitys}')
    # print(f'Нулевая волатильность: \n {zero}')

    for volater in volaters:
        volater.join()


if __name__ == '__main__':
    main()
