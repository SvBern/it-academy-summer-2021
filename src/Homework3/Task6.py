# Упорядоченный список
# Дан список целых чисел. Требуется переместить все ненулевые
# элементы в левую часть списка, не меняя их порядок,
# а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя,
# список использовать нельзя, задачу нужно выполнить
# за один проход по списку. Распечатайте полученный список.

list1 = [1, 0, 2, 0, 3, 4, 0]

for i in list1:
    if list1[i] == 0:
        list1.append(list1[i])
        del list1[i]

print(list1)
