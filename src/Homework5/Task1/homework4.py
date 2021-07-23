def cubed_of_num():
    """Dict comprehensions

    Создайте словарь с помощью генератора словарей,
    так чтобы его ключами были числа от 1 до 20,
    а значениями кубы этих чисел.
    """
    print({item: item ** 3 for item in range(1, 21)})


def check_country(**kwargs):
    """Города.
    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.
    Входные данные:
    Программа получает на вход количество стран N.
    Далее идет N строк, каждая строка начинается с названия страны,
    затем идут названия городов этой страны.
    В следующей строке записано число M,
    далее идут M запросов — названия каких-то M городов, перечисленных выше.
    Выходные данные:
    Для каждого из запроса выведите название страны,
    в котором находится данный город.
    Примеры:
    Входные данные
    2
    Russia Moscow Petersburg Novgorod Kaluga
    Ukraine Kiev Donetsk Odessa
    3
    Odessa
    Moscow
    Novgorod
    Выходные данные
    Ukraine
    Russia
    Russia
    """
    if not kwargs:
        kwargs = ['Russia Moscow Petersburg Novgorod Kaluga', 'Ukraine Kiev Donetsk Odessa']
    country_city_dict = {}
    for item in kwargs:
        country = item.split()
        country_city_dict[country[0]] = country[1:]

    name_city_list = ['Odessa', 'Moscow', 'Novgorod']
    for name_city in name_city_list:
        for country, cities in country_city_dict.items():
            if name_city in cities:
                print(country)


def count_diff_num(str1='1234', str2='12356'):
    """Даны два списка чисел. Посчитайте, сколько различных чисел
    содержится одновременно как в первом списке, так и во втором.
    """
    print(len(set(str1.split()) | set(str2.split())))


def diff_num_in_one(str1='1234', str2='12356'):
    """Даны два списка чисел.
    Посчитайте, сколько различных чисел
    входит только в один из этих списков
    """
    print(len(set(str1.split()) - set(str2.split())))


def pupils_languages(**kwargs):
    """Языки.

    Каждый из N школьников некоторой школы знает Mi языков.
    Определите, какие языки знают все школьники и языки,
    которые знает хотя бы один из школьников.
    Входные данные
    Первая строка входных данных содержит количество школьников N.
    Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
    содержащих названия языков, которые знает i-й школьник.
    Пример входных данных: 3      # N количество школьников
    2          # M1 количество языков первого школьника
    Russian    # языки первого школьника
    English
    3          # M2 количество языков второго школьника
    Russian
    Belarusian
    English
    3
    Russian
    Italian
    French
    Выходные данные
    В первой строке выведите количество языков, которые знают все школьники.
    Начиная со второй строки - список таких языков.
    Затем - количество языков, которые знает хотя бы один школьник,
    на следующих строках - список таких языков.
    """
    if not kwargs:
        kwargs = {'pupil_1': ['Russian', 'English'],
                  'pupil_2': ['Russian', 'Belarusian', 'English'],
                  'pupil_3': ['Russian', 'Italian', 'French']}
    list_of_languages = []
    for languages in kwargs.values():
        list_of_languages.append(set(languages))

    com_lang = set.intersection(*list_of_languages)
    print('Языков, которые знают все: ', len(com_lang), 'шт')
    for languages_name in com_lang:
        print(languages_name)

    at_least_one = set.union(*list_of_languages)
    print('Языков, которыми владеет хотя бы один человек: ',
          len(at_least_one), 'шт')
    for language_name in at_least_one:
        print(language_name)


def diff_words(text='Во входной строке записан текст.'):
    """Во входной строке записан текст.
    Словом считается последовательность
    непробельных символов идущих подряд, слова разделены одним
    или большим числом пробелов или символами конца строки.
    Определите, сколько различных слов содержится в этом тексте.
    """
    text = text.lower().split()
    counter_words = set()
    for word in text:
        if word.isalpha() is True:
            counter_words.add(word)
    print('В тексте', len(counter_words), 'разных слов')


def euclidean_algorithm(num1=20, num2=16):
    """Оглянемся назад. Числа.
    Даны два натуральных числа. Вычислите их наибольший общий делитель
    при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    print(num1 + num2)
