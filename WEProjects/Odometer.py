''' Write a set of functions so that a programmer who needs an odometer, with the
above characteristics, can use those functions to implement the same. At the
minimum, the following functions need to be written:
• next reading() to find the next reading for a given reading. Should
return 2468 for 2467 and 2567 for 2489.
• prev reading() tofind the previous reading for a given reading. Should
return 378 for 379 and 289 for 345.
• nth reading after(r) Instead of the next reading, return the reading
that occurs after r rotations. The next reading can be thought of as a
special case: r = 1
• nth reading before(r) Similar to above.
• distance() Given two readings find the number of readings between
them. Note that just subtracting the readings will be wrong often. You
also need to handle the fact that the distance from 789 to 123 is 1, while
the distance from 123 to 789 is different. If different sized readings are
given return -1.
'''
class Odometer:
    def __init__(self, size):
        DIGITS = "123456789"
        self.SIZE = size
        self.START = int(DIGITS[:size])
        self.LIMIT = int(DIGITS[-size:])
        self.reading = self.START

    def __repr__(self):
        return f'{self.START}<{self.reading}>{self.LIMIT}'

    def __str__(self):
        return str(self.reading)

    def forward(self, steps=1):
        for _ in range(steps):
            if self.reading == self.LIMIT:
                self.reading = self.START
            else:
                self.reading += 1
                while not is_ascending(self.reading):
                    self.reading += 1

    def backward(self, steps=1):
        for _ in range(steps):
            if self.reading == self.START:
                self.reading = self.LIMIT
            else:
                self.reading -= 1
                while not is_ascending(self.reading):
                    self.reading -= 1

    def distance(self, other) -> int:
        if self.SIZE != other.SIZE:
            return -1
        self_copy = Odometer(self.SIZE)
        self_copy.reading = self.reading
        diff = 0
        while self_copy.reading != other.reading:
            self_copy.forward()
            diff += 1
        return diff
    
@staticmethod
def is_ascending(n: int) -> bool:
    sn = str(n)
    return all([a < b for a, b in zip(sn, sn[1:])])

class Reading:
    def __init__(self, size):


o = Odometer(4)
print(is_ascending(122))
o.forward()
print(o)
o.backward()
print(o)


