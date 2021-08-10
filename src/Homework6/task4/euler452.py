from collections import defaultdict
from math import sqrt

"""Задача 452 Длинные произведения

Определим F(m,n) как количество кортежей положительных чисел длиной n,
произведение всех элементов которых не превышает m.
F(10, 10) = 571.
F(106, 106) mod 1 234 567 891 = 252903833.
Найдите F(109, 109) mod 1 234 567 891.
__________________________________________________
Обобщите указанную задачу на свое усмотрение,
решите ее, покройте тестами.
"""


def euler_452(limit):
    """Программа возвращает количество кортежей(без деления)"""
    d = defaultdict(int)
    chain = [0]

    def f(prod, p):
        if prod * p <= limit:
            chain[-1] += 1
            d[tuple(chain)] += 1
            f(prod * p, p)
            chain[-1] -= 1
            chain.append(1)
            for newp in range(p + 1, int(sqrt(limit // prod)) + 1):
                f(prod * newp, newp)
            d[tuple(chain)] += limit // prod - p
            chain.pop()

    f(1, 2)
    tot = 1
    for profile, cnt in d.items():
        for i in range(limit, limit - sum(profile), - 1):
            cnt *= i
        for i in profile:
            for j in range(i, 1, -1):
                cnt //= j
        tot += cnt
    return tot
