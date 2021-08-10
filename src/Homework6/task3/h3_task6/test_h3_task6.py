import ddt
from Homework6.task3.h3_task6 import h3_task6
import unittest
"""
Оформите указанную задачу из прошлых домашних в виде функции
и покройте тестами. Учтите, что в функцию могут быть переданы
некорректные значения, здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила
все возможные ситуации сама.
"""


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(
        ([1, 0, 1], [1, 1, 0]),
        ([1, 1, 2], [1, 1, 2]),
        ([], []),
    )
    @ddt.unpack
    def test_1(self, input_data, expected):
        """Тест на правильную работу: ввод двух различных списков, пустой список"""
        result = h3_task6.sorting_numbers(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (2, TypeError),
        ({1, 2, 3, 4, 1, 2}, TypeError),
    )
    @ddt.unpack
    def test_2(self, input_data, expected):
        """Тест на отрицательный результат: вводится число, сет"""
        with self.assertRaises(expected):
            h3_task6.sorting_numbers(input_data)


if __name__ == '__main__':
    unittest.main()
