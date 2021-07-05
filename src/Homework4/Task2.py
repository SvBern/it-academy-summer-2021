""" Города.

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
count_country = int(input('Введите количество стран: \n'))

country_city_dict = {}
for counter in range(count_country):
    country = input('Введите через пробелы страну и её города: \n').split()
    country_city_dict[country[0]] = country[1:]

count_city = int(input('Введите количество проверяемых городов: \n'))

city_list = []
for counter in range(count_city):
    name_city = input('Введите название города:  \n')
    city_list.append(name_city)
    for key, value in country_city_dict.items():
        if city_list[counter] in value:
            print(key)
