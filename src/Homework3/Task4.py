# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество  пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

str1 = input('Введите любые числа через пробел\n')

temp = []
[temp.append(element) for element in str1.split()]

counter = 0
for item in range(len(temp)):
    for item1 in range(item + 1, len(temp)):
        if temp[item] == temp[item1]:
            counter += 1
print(counter, 'пар чисел в этом списке')
