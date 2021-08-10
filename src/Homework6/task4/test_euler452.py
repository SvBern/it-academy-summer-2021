import ddt
import euler452
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
        (3, 7),
        (10, 571),
    )
    @ddt.unpack
    def test_1(self, input_data, expected):
        """
        Тест на положительный результат:
        вводятся значения с заведомо известным результатом
        """
        result = euler452.euler_452(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ([], TypeError),
        ({1, 2, 3, 4, 1, 2}, TypeError),
        ({}, TypeError),
        ('sss', TypeError),
        (0, TypeError),

    )
    @ddt.unpack
    def test_2(self, input_data, expected):
        """Тест на отрицательный результат"""
        with self.assertRaises(expected):
            euler452.euler_452(input_data)


if __name__ == '__main__':
    unittest.main()