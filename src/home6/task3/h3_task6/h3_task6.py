class NotIntErrors(Exception):
    pass


def sorting_numbers(list_int):
    """Упорядоченный список.

    Дан список целых чисел. Требуется переместить все ненулевые
    элементы в левую часть списка, не меняя их порядок,
    а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя,
    список использовать нельзя, задачу нужно выполнить
    за один проход по списку. Распечатайте полученный список.
    """
    for i in list_int:
        if type(i) is int:
            if list_int[i] == 0:
                list_int.append(list_int[i])
                del list_int[i]
        else:
            raise NotIntErrors("Введено не целое число")
    return list_int
