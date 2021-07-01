# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник.
# Пример входных данных: 3          # N количество школьников
# 2          # M1 количество языков первого школьника
# Russian    # языки первого школьника
# English
# 3          # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник,
# на следующих строках - список таких языков.

count_children = int(input('Введите количество школьников: \n'))

list_of_languages = []
for children in range(1, count_children + 1):
    count_languages = int(input(f'Введите кол-во языков, которыми владеет ученик {children}: \n'))
    name_language = set()
    for language in range(count_languages):
        name_language.add(input('Введите название языка: \n'))
    list_of_languages.append(name_language)

common_languages = set.intersection(*list_of_languages)
print('Языков, которые знают все: ', len(common_languages), 'шт')
for language_name in common_languages:
    print(language_name)

diff_languages = set.difference(*list_of_languages)
print('Языков, которыми владеет только один человек: ', len(diff_languages), 'шт')
for language_name in diff_languages:
    print(language_name)
