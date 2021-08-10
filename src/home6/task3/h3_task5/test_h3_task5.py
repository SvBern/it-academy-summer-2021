import ddt
from home6.task3.h3_task5 import h3_task5
import unittest


@ddt.ddt
class Test(unittest.TestCase):
    """
    Оформите указанную задачу из прошлых домашних в виде функции
    и покройте тестами. Учтите, что в функцию могут быть переданы
    некорректные значения, здесь может пригодится ‘assertRaises’.
    Не нужно переделывать функцию для того чтобы она ловила
    все возможные ситуации сама.
    """
    @ddt.data(
        (['a', 'n', 'n'], ['a']),
        ([], []),
        ([1, 2, 2, 3], [1, 3]),
        ('1231', ['2', '3']),
    )
    @ddt.unpack
    def test_1(self, input_data, expected):
        """Тест на положительный результат работы"""
        result = h3_task5.unique_elements(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (2, TypeError),
        ({1, 2, 2, 3}, AttributeError),
    )
    @ddt.unpack
    def test_2(self, input_data, expected):
        """Тест на отрицательный результат работы. Нашла только 1 вариант"""
        with self.assertRaises(expected):
            h3_task5.unique_elements(input_data)


if __name__ == '__main__':
    unittest.main()
