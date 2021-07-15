def power_of_two(num):
    """

    :param num: int
    :return: int
    Написать программу которая находит ближайшую степень
    двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)

    """
    # получение ближайшего большего числа в степени 2
    most_power = 2 ** num.bit_length()
    # получение ближайшего меньшего числа
    temp = num.bit_length() - 1
    low_power = 1
    for i in range(temp):
        low_power *= 2
    # проверка, какое число ближе к введенному
    if num - low_power < most_power - num:
        print(f'Ближайшая к {num} степень двойки число: ', low_power)
    else:
        print(f'Ближайшая к {num} степень двойки число: ', most_power)


power_of_two(int(input('Введите число: ')))
