from math import floor
import time


class DecimalClock:
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

    def dectime_scale(self, dectime, scale, limit=10):
        return floor(dectime * scale % limit)

    def set_current_time(self):
        now = time.time() / 1.25  # 1 disec = 1.25 seconds
        self.disec = self.dectime_scale(now, 1)
        self.dimin = self.dectime_scale(now, 1/10)
        self.dihor = self.dectime_scale(now, 1/100)
        self.didec = self.dectime_scale(now, 1/1000, 69.12)
        self.didia = self.dectime_scale(now, 1/10000, 365.25)

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

    def get_full_time(self):
        return f"{self.didia:.0f}dd {self.didec:.0f}dc {self.dihor:.0f}dh {self.dimin:.0f}dm {self.disec:.0f}ds {self.corchea:.0f}sc"

    def get_time(self):
        def add_zeros(x): return "0" + str(x) if x < 10 else str(x)
        return f"{add_zeros(self.didec)}:{add_zeros(self.dihor)}:{add_zeros(self.dimin)}"


if __name__ == "__main__":
    clock = DecimalClock()
    clock.set_current_time()
    while True:
        clock.tick()
        print(clock.get_full_time(), f"[{clock.get_time()}]")
