from math import floor
import time
import sys

class Clock:
    def __init__(self):
        self.didec = 0
        self.didia = 0
        self.dihor = 0
        self.dimin = 0
        self.disec = 0
        self.corchea = 0
        self.tempo = 90
        self.tempo = self.tempo/60
        self.tempo = self.tempo/4

    def dtime_scale(self, time, scale, limit=10):
        return floor(time * scale % limit)

    def set_current_time(self):
        dtime = time.time() / 1.25
        self.disec = self.dtime_scale(dtime, 1)
        self.dimin = self.dtime_scale(dtime, 1/10)
        self.dihor = self.dtime_scale(dtime, 1/100)
        self.didec = self.dtime_scale(dtime, 1/1000, 69.12)
        self.didia = self.dtime_scale(dtime, 1/10000, sys.maxsize)

    def tick(self):
        self.corchea += 1
        if self.corchea == 4:
            self.corchea = 0
            self.disec += 1
        if self.disec >= 9:
            self.disec = 0
            self.dimin += 1
        if self.dimin >= 9:
            self.dimin = 0
            self.dihor += 1
        if self.dihor >= 9:
            self.dihor = 0
            self.didec += 1
        if self.didec >= 69.12:
            self.didec = 0
            self.didia += 1
        time.sleep(self.tempo)

    def get_time(self):
        return f"{self.didia:.0f}dd {self.didec:.0f}dc {self.dihor:.0f}dh {self.dimin:.0f}dm {self.disec:.0f}ds {self.corchea:.0f}sc"


if __name__ == "__main__":
    clock = Clock()
    clock.set_current_time()
    while True:
        clock.tick()
        print(clock.get_time())
