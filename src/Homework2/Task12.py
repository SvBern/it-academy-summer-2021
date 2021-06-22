# Недавно открытый международный бренд решил создать
# логотип своей компании на трех наиболее
# распространенных символах в названии компании.
# Сейчас они пробуют различные комбинации
# названий компаний и логотипов на основе этого условия.
# Учитывая строку, то есть название компании
# строчными буквами,
# ваша задача - найти три самых распространенных символа в строке.
# Выведите три самых распространенных символа
# и количество их вхождений.
# Сортировать по убыванию количества вхождений.
# Если количество вхождений такое же,
# отсортируйте символы в алфавитном порядке.
# Например, согласно условиям, описанным выше,
# GOOGLE был бы логотип с буквами GOE.
# Формат ввода
# Одна строка ввода, содержащая строку .
# Ограничения: 1. строка имеет имеет по крайней мере 3 разных символа;
# 2. Длина строки не менее 3-х символов и не более 10 в 4 степени.
# Выходной формат
# Выведите три самых распространенных символа вместе с количеством
# их появления каждый в отдельной строке.
# Сортировка вывода в порядке убывания количества вхождений.
# Если количество вхождений такое же,
# отсортируйте символы в алфавитном порядке.порядке.

str1 = input('Введите название компании строчными буквами\n')

if len(str1) < 3:
    print('Название компании слишком короткое!')
elif len(str1) > (10 ** 2) ** 2:
    print('Название компании слишком длинное!')
else:
    MyList = list(str1.strip())  # преобразую строку в список
    temp = []
    # новый список, отсортированы только буквы
    [temp.append(x) for x in MyList if x.isalpha() is True]
    # список, отсортированный по алфавиту
    list_alphabet = sorted(temp)
    # вторая сортировка по количеству вхождений
    list_count = sorted(list_alphabet, key=list_alphabet.count, reverse=True)
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
