import time
from threading import Thread

class Knight(Thread):

    def __init__(self, name, power):
        self.name_r = name
        self.power = power
        super().__init__()

    def run(self):
        count_enemies = 100
        count_day = 0
        print(f'{self.name_r}, на нас напали!')
        while count_enemies > 0:
            count_enemies -= self.power
            count_day += 1
            print(f'{self.name_r} сражается {count_day} дней(дня), осталось {count_enemies} воинов.')
            time.sleep(1)
            if count_enemies == 0:
                print(f'{self.name_r} одержал победу спустя {count_day} дней(дня)!' )

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread_1 = first_knight
thread_2 = second_knight

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f'Все битвы закончились!')