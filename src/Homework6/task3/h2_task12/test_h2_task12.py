import ddt
from Homework6.task3.h2_task12 import h2_task12
import unittest


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(
        ('test', ['t', 'e', 's']),
        ('test1111111111', ['t', 'e', 's']),
        ('coca cola', ['c', 'a', 'o']),
    )
    @ddt.unpack
    def test_1(self, input_data, expected):
        """Тест на правильную работу: три варианта с разными строками"""
        result = h2_task12.logo(input_data)
        self.assertEqual(result, expected)

    @ddt.data((123, TypeError),
        ([1, 2, 2, 3], AttributeError),
        ('1231123', IndexError),
    )
    @ddt.unpack
    def test_2(self, input_data, expected):
        """Тест на непр.работу: ошибка при вводе числа, списка, строки без букв"""
        with self.assertRaises(expected):
            h2_task12.logo(input_data)


if __name__ == '__main__':
    unittest.main()
