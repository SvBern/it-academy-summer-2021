# Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются
# в списке только один раз. Элементы нужно выводить в том порядке,
# в котором они встречаются в списке.

list1 = list(input('Введите любые символы\n'))

temp_list = []
for element in list1:
    if list1.count(element) == 1 and element not in temp_list:
        temp_list.append(element)

print(temp_list)
