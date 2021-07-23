def count_cost_goods(pieces=3, rubl=22, kopek=30):
    """The total amount of purchases
    Returns the total amount of purchases after entering
    the quantity of goods (pieces) and prices in rubles and
    """
    pieces, rubl, kopek = int(pieces), int(rubl), int(kopek)
    cost = pieces * (100 * rubl + kopek)
    print('Общая сумма покупки:', cost // 100, 'руб', cost % 100, 'коп')


def more_long_word(sentence='Returns the longest word in a sentence'):
    """Returns the longest word (long_word) in a sentence"""
    long_word = max(sentence.split(), key=len)
    print("Самое длинное слово в предложении: ", long_word)


def deleting_repeats(str1='Returns a string with repetitions removed'):
    """Returns a string with repetitions removed"""
    new_str = ''
    for element in str1:
        if element not in new_str and element != ' ':
            new_str += element
    print(new_str)


def counter_letters(str1='Returns the number of uppercase and lowercase'):
    """Returns the number of uppercase and lowercase
    letters from the entered string
    """
    low_letter = 0
    up_letter = 0
    for element in str1:
        if 'a' <= element <= 'z':
            low_letter += 1
        if 'A' <= element <= 'Z':
            up_letter += 1
    print('Количество строчных букв:', low_letter)
    print('Количество прописных букв:', up_letter)


def fibonacci(num=5):
    """the Fibonacci number
    Returns the Fibonacci number with
    the given ordinal
    """
    if num == 1:
        fib_2 = 0
    else:
        fib_1 = 0
        fib_2 = 1
        counter = 0
        while counter < num - 2:
            fib = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib
            counter += 1
    print(f'Значение числа Фибоначчи с порядковым номером {num}:', fib_2)


def palindrome(num=2552):
    """Palindrome
    Determines if the entered number (num) is a palindrome
    """
    temporarily = num
    reverse = 0
    while num > 0:
        rest = num % 10
        reverse = reverse * 10 + rest
        num = num // 10
    if reverse == temporarily:
        print('Это число - палиндром!')
    else:
        print('Это не палиндром!')


def area_of_a_triangle(a=3, b=4, c=5):
    """Determines the existence of a triangle and its area"""
    if a + b > c and a + c > b and c + b > a:
        p = (a + b + c) / 2
        area_tr = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('Это треугольник!\n')
        print('Площадь этого треугольника:', area_tr)
    else:
        print('Это не треугольник!')


def numbers(num=24):
    """Task/
    Given an integer, , perform the following conditional actions:
    If  is odd, print Weird
    If  is even and in the inclusive range of  2 to 5, print Not Weird
    If  is even and in the inclusive range of  6 to 20, print Weird
    IF  is even and greater than 20, print Not Weird
    Input Format
    A single line containing a positive integer, .
    Constraints
    Output Format
    Print Weird if the number is weird. Otherwise, print Not Weird.
    """
    if 1 <= num <= 100:
        if num % 2 == 1:
            print('Weird')
        else:
            if 2 <= num <= 5 or num > 20:
                print('Not weird')
            elif 6 <= num <= 20:
                print('Weird2')
    else:
        print('Bad num')


def middle_of_a_word(str1='middle'):
    """Returns the middle character of a word
    if the word has an even number of characters,
    two middle characters
    if the word has an odd number of characters
    """
    counter = int(len(str1))
    if counter % 2 == 0:
        middle = counter / 2
        previous_item = middle - 1
        print(str1[int(previous_item)] + str1[int(middle)])
    else:
        middle_element = counter // 2
        print(str1[int(middle_element)])


def determine_the_century(year=2021):
    """Век из года
    Первые пролеты века от года 1 до и включая 100 года ,
    второй - от года до 101 включительно 200 года , и т.д.
    Задача :
    Учитывая год, верните век, в котором он находится.
    """
    if year > 0:
        ten = year // 100
        century = ten + 1
        print(f'Это {century} век!')
    else:
        print('Вы ввели неправильное значение')


def isogram(str1='функция'):
    """Изограммы
    Изограмма - это слово, в котором
    нет повторяющихся букв,
    последовательных или непоследовательных.
    Реализуйте функцию, которая определяет,
    является ли строка, содержащая только буквы, изограммой.
    Предположим, что пустая строка является изограммой.
    Игнорировать регистр букв.
    """
    new_str = ''
    for element in str1.casefold():
        if element not in new_str:
            new_str += element
    if len(str1) == len(new_str):
        print('Это изограмма!')
    else:
        print('Это не изограмма!')


def logo(str1='new international brand'):
    """Недавно открытый международный бренд решил создать
    логотип своей компании на трех наиболее
    распространенных символах в названии компании.
    Сейчас они пробуют различные комбинации
    названий компаний и логотипов на основе этого условия.
    Учитывая строку, то есть название компании строчными буквами,
    задача - найти три самых распространенных символа в строке.
    Выведите три самых распространенных символа
    и количество их вхождений.
    Сортировать по убыванию количества вхождений.
    Если количество вхождений такое же,
    отсортируйте символы в алфавитном порядке.
    Например, согласно условиям, описанным выше,
    GOOGLE был бы логотип с буквами GOE.
    Формат ввода.
    Одна строка ввода, содержащая строку .
    Ограничения: 1. строка имеет имеет по крайней мере 3 разных символа;
    2. Длина строки не менее 3-х символов и не более 10 в 4 степени.
    Выходной формат
    Выведите три самых распространенных символа вместе с количеством
    их появления каждый в отдельной строке.
    Сортировка вывода в порядке убывания количества вхождений.
    Если количество вхождений такое же,
    отсортируйте символы в алфавитном порядке
    """
    if len(str1) < 3:
        print('Название компании слишком короткое!')
    elif len(str1) > (10 ** 2) ** 2:
        print('Название компании слишком длинное!')
    else:
        my_list = list(str1.strip())  # преобразую строку в список
        temp = []
        # новый список, отсортированы только буквы
        [temp.append(x) for x in my_list if x.isalpha() is True]
        # список, отсортированный по алфавиту
        list_alphabet = sorted(temp)
        # вторая сортировка по количеству вхождений
        list_count = sorted(list_alphabet, key=list_alphabet.count,
                            reverse=True)
        # создаю словарь "буква:количество"
        dictionary = {i: list_count.count(i) for i in list_count}
        new_list = list(dictionary)
        new_num = list(dictionary.values())
        print(f'Самая частая буква: {new_list[0]},'
              f' повторяется {new_num[0]} раз')
        print(f'Самая частая буква № 2: {new_list[1]}, '
              f'повторяется {new_num[1]} раз')
        print(f'Самая частая буква № 3: {new_list[2]}'
              f' повторяется {new_num[2]} раз')
        print(f'Ваш логотип: {new_list[0] + new_list[1] + new_list[2]}')
