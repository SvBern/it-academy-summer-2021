"""Оформите указанную задачу из прошлых домашних в виде функции

и покройте тестами. Учтите, что в функцию могут быть переданы
некорректные значения, здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила
все возможные ситуации сама.
Тестируется задача 12 из домашней работы 2
"""
import ddt
from home6.task3.h2_task12 import h2_task12
import unittest


@ddt.ddt
class TestInput(unittest.TestCase):
    """Класс тестирует входящие данные"""
    @ddt.data(
        ('test', ['t', 'e', 's']),
        ('test1111111111', ['t', 'e', 's']),
        ('coca cola', ['c', 'a', 'o']),
    )
    @ddt.unpack
    def test_input_positiv(self, input_data, expected):
        """Тест на правильную работу: три варианта с разными строками"""
        result = h2_task12.logo(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (123, TypeError),
        ([1, 2, 2, 3], AttributeError),
        ('1231123', IndexError),
        )
    @ddt.unpack
    def test_input_negativ(self, input_data, expected):
        """Тест на непр.работу: ошибка при вводе

        числа, списка, строки без букв
        """
        with self.assertRaises(expected):
            h2_task12.logo(input_data)


if __name__ == '__main__':
    unittest.main()
