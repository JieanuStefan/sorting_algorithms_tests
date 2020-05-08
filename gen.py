import sys

from random import randrange
from math import sin

sys.setrecursionlimit(10000)


def random(count):
    with open('list.txt', 'w') as f:
        f.write('')

    with open('list.txt', 'a') as f:
        for _ in range(0, count):
            n = str(randrange(1000000))
            f.write(n + ' ')


def mostly_sorted(count):
    with open('list.txt', 'w') as f:
        f.write('')

    with open('list.txt', 'a') as f:
        for i in range(0, count):
            r = randrange(100)
            if (r > 90):
                f.write(str(randrange(count)) + ' ')
            else:
                f.write(str(i) + ' ')

        
def sin_pattern(count):
    with open('list.txt', 'w') as f:
        f.write('')

    with open('list.txt', 'a') as f:
        for i in range(0, count):
            f.write(str(int(sin(i) * 10000)) + ' ')


def half_half(count):
    with open('list.txt', 'w') as f:
        f.write('')

    with open('list.txt', 'a') as f:
        for i in range(count // 2, count):
            f.write(str(i) + ' ')
        for i in range(0, count // 2):
            f.write(str(i) + ' ')