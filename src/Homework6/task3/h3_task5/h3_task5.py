def unique_elements(list1):
    """Уникальные элементы в списке

    Дан список. Выведите те его элементы, которые встречаются
    в списке только один раз. Элементы нужно выводить в том порядке,
    в котором они встречаются в списке.
    """
    temp_list = []
    for element in list1:
        if list1.count(element) == 1:
            temp_list.append(element)
    return temp_list
