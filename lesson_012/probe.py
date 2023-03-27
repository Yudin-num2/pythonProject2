import os
from operator import itemgetter
from pprint import pprint
import time
import threading


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class Volater(threading.Thread):

    def __init__(self, f, lock, all_volatilitys, zero, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = f
        self.sorted_total_prices = []
        self.all_volatilitys = all_volatilitys
        self.zero_volatility = zero
        self.lock_all_volatilitys = lock

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
            with self.lock_all_volatilitys:
                self.zero_volatility[self.f] = volatility
        else:
            with self.lock_all_volatilitys:
                self.all_volatilitys[self.f] = volatility


lock = threading.Lock()
all_volatilitys = {}
zero = {}
path_to_directory = 'trades'
all_files = []


@time_track
def main():

    for dirname, dirpath, files in os.walk(path_to_directory):
        for file in files:
            all_files.append(file)

    volaters = [Volater(f=f, lock=lock, all_volatilitys=all_volatilitys, zero=zero, daemon=True) for f in all_files]

    for volater in volaters:

        volater.start()
    for volater in volaters:
        volater.join()

    max_volatilitys = sorted(all_volatilitys.items(), key=itemgetter(1))[-1:-4:-1]
    min_volatilitys = sorted(all_volatilitys.items(), key=itemgetter(1))[0:3]

    print(f'Максимальная волатильность: \n {max_volatilitys}')
    print(f'Минимальная волатильность: \n {min_volatilitys}')
    print(f'Нулевая волатильность: \n {zero}')


if __name__ == '__main__':
    main()