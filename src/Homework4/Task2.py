# Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны.
# В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны,
# в котором находится данный город.
# Примеры
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod
# Выходные данные
# Ukraine
# Russia
# Russia

count_country = int(input('Введите количество стран: \n'))

country_city_dict = {}
for counter in range(1, count_country+1):
    country = input('Введите через пробелы страну и её города: \n').split()
    country_city_dict |= dict.fromkeys(country[1:], country[0])

count_city = int(input('Введите количество проверяемых городов: \n'))

country_list = ""
for counter in range(1, count_city+1):
    name_city = input('Введите название города:  \n')
    country_list += country_city_dict[name_city] + '\n'

print(country_list)
