def fizz_buzz():
    """Fizz/Buzz/FizzBuzz

    В заданном числовом промежутке находит числа,
    кратные 3/5/15 и заменяет их
    словами Fizz/Buzz/FizzBuzz соответственно
    """
    num1, num2 = 1, 101
    list1 = []
    for i in range(num1, num2):
        if i % 15 == 0:
            list1.append('FizzBuzz')
        elif i % 3 == 0:
            list1.append('Fizz')
        elif i % 5 == 0:
            list1.append('Buzz')
        else:
            list1.append(i)
    for element in list1:
        print(element)


def addition_of_letters():
    """Используйте генератор списков,

    чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].)
    """
    str1, str2 = 'ab', 'bcd'
    list1 = [x + y for x in str1 for y in str2]
    print(list1)


def cut_syllables():
    """Используйте на предыдущий список slice

    чтобы получить следующий: ['ab', 'ad', 'bc'].
    """
    list1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
    list2 = list1[::2]
    print(list2)


def num_letter():
    """Используйте генератор списков,

    чтобы получить следующий ['1a', '2a', '3a', '4a'].
    """
    str_letter = 'a'
    list3 = [str(x) + str_letter for x in range(5) if x != 0]
    print(list3)


def cut_element():
    """Одной строкой удалите элемент '2a'

    из прошлого списка и напечатайте его.
    """
    list4 = ['1a', '2a', '3a', '4a']
    print(list4.pop(1))


def copy_list():
    """Скопируйте список и добавьте в него элемент

    '2a' так, чтобы в исходном списке этого элемента
    не было.
    """
    list_num = ['1a', '3a', '4a']
    new_list = list_num.copy()
    new_list[1:1] = ['2a']
    print('list3:', list_num)
    print('list4:', new_list)


def do_list_and_tuple():
    """Создайте список ['a', 'b', 'c']

    и сделайте из него кортеж.
    """
    list_1 = ['a', 'b', 'c']
    cort_1 = tuple(list_1)
    print(type(list_1), list_1)
    print(type(cort_1), cort_1)


def do_tuple_and_list():
    """Создайте кортеж ('a', 'b', 'c') и

    сделайте из него список
    """
    cort2 = ('a', 'b', 'c')
    list2 = [cort2]
    print(type(cort2), cort2)
    print(type(list2), list2)


def value_of_var():
    """Присвоение значений (a, b, c)

    переменным одной строкой
    a = 'a', b=2, c=’python’
    """
    a, b, c = 'a', int(2), 'python'
    print('a =', a, 'b =', b, 'c =', c)


def output_numbers():
    """Создает кортеж из одного элемента,

    при итерировании
    по этому элементу последовательно выводятся значения 1, 2, 3.
    len() исходного кортежа возвращает 1.
    """
    cort2 = ([1, 2, 3],)
    print(len(cort2), type(cort2))
    for i in cort2[0]:
        print(i)


def couple_of_element():
    """Пары элементов

    Дан список чисел. Посчитайте, сколько в нем пар элементов,
    равных друг другу. Считается, что любые два элемента,
    равные друг другу образуют одну пару, которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    """
    list1 = list(input('Введите любые числа через пробел\n'))
    temp = []
    [temp.append(element) for element in list1 if element != ' ']

    counter = 0
    for item in range(len(temp)):
        for item1 in range(item + 1, len(temp)):
            if temp[item] == temp[item1]:
                counter += 1
    print(counter, 'пар чисел в этом списке')


def unique_elements():
    """Уникальные элементы в списке

    Дан список. Выведите те его элементы, которые встречаются
    в списке только один раз. Элементы нужно выводить в том порядке,
    в котором они встречаются в списке.
    """
    list_elem = list(input('Введите любые символы\n'))
    temp_list = []
    for element in list_elem:
        if list_elem.count(element) == 1:
            temp_list.append(element)
    print(temp_list)


def sorting_numbers():
    """Упорядоченный список.

    Дан список целых чисел. Требуется переместить все ненулевые
    элементы в левую часть списка, не меняя их порядок,
    а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя,
    список использовать нельзя, задачу нужно выполнить
    за один проход по списку. Распечатайте полученный список.
    """
    list_int = [1, 0, 2, 0, 3, 4, 0]
    for i in list_int:
        if list_int[i] == 0:
            list_int.append(list_int[i])
            del list_int[i]
    print(list_int)
