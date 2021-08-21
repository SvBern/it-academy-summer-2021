"""Задача 452 Длинные произведения.

Определим F(m,n) как количество кортежей положительных чисел длиной n,
произведение всех элементов которых не превышает m.
F(10, 10) = 571.
F(106, 106) mod 1 234 567 891 = 252903833.
Найдите F(109, 109) mod 1 234 567 891.
___________________________________________
Обобщите указанную задачу на свое усмотрение, решите ее, покройте тестами
"""
from functools import lru_cache
from functools import reduce
import itertools


@lru_cache(maxsize=None)
def euler_452(n, m):
    digits = []
    # формируется список из значений от 1 до n включительно, каждое значение
    # повторяется n раз
    digits += [i for i in range(1, n + 1)] * n
    # генерируются кортежи со всеми возможными перестановками, элементы каждого
    # кортежа перемножаются, отсортировываются только те, где произведение не
    # превышает n
    list_of_cort = [item for item in
                    itertools.combinations_with_replacement(digits, n)
                    if reduce(lambda x, y: y * x, item) <= m]
    set_of_cort = set(list_of_cort)  # удаляем одинаковые кортежи
    return len(set_of_cort)
