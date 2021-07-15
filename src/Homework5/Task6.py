def divider_power_of_two(num):
    """Вводится число найти его максимальный делитель,

     являющийся степенью двойки. 10(2) 16(16), 12(4).
     """
    # получение ближайшего меньшего числа
    temp = num.bit_length() - 1
    low_power = 1
    for i in range(temp):
        low_power *= 2
    # проверка, делитель ли, иначе берем другое число
    while num % low_power != 0:
        low_power *= 0.5
    print(f'Наибольший делитель числа {num},'
          f'являющийся степенью двойки: ', int(low_power))


divider_power_of_two(int(input('Введите число: ')))
