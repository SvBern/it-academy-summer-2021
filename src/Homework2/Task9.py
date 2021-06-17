# Получите средний персонаж
# Вам дадут слово. Ваша задача - вернуть средний символ слова.
# Если длина слова нечетная, вернуть средний символ.
# Если длина слова четная, вернуть 2 средних символа.

str1 = input('Введите любое слово\n')

counter = int(len(str1))
if counter % 2 == 0:
    middle = counter / 2
    previous_item = middle - 1
    print(str1[int(previous_item)] + str1[int(middle)])
else:
    middle_element = counter // 2
    print(str1[int(middle_element)])
