import ddt
import euler452_my_solution
import unittest


@ddt.ddt
class TestInput(unittest.TestCase):
    @ddt.data(
        (2, 2, 3),
        (3, 3, 7),
    )
    @ddt.unpack
    def test_input_positiv(self, input_data1, input_data2, expected):
        """Тест на положительный результат:

        вводятся значения с заведомо известным результатом
        """
        result = euler452_my_solution.euler_452(input_data1, input_data2)
        self.assertEqual(result, expected)

    @ddt.data(
        ([], [], TypeError),
        ({1, 2, 3, 4, 1, 2}, {1, 2, 3}, TypeError),
        ({}, {}, TypeError),
        ('sss', '', TypeError),
        (0, 0, TypeError),
    )
    @ddt.unpack
    def test_input_negativ(self, input_data1, input_data2, expected):
        """Тест на отрицательный результат"""
        with self.assertRaises(expected):
            euler452_my_solution.euler_452(input_data1, input_data2)


if __name__ == '__main__':
    unittest.main()
