import time as t


class MyTimer():
    def __init__(self):
        self.unit = ['year', 'month', 'day', 'hours', 'minute', 'sec']
        self.prompt = 'wei kaishi jishi '
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        self.prompt = 'pleasd stop!'
        print("jishikaishi")

    def stop(self):
        if not self.begin:
            print('please start')
        else:
            self.end = t.localtime()
            self._calc()
            print("jishijieshu")

    def _calc(self):
        self.lasted = []
        self.prompt = 'zonggongyunxingle'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])

            self.begin = 0
            self.end = 0



