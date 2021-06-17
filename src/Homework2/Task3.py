str1 = input('Введите любую строку:')

new_str = ''
for element in str1:
    if element not in new_str and element != ' ':
        new_str += element

print(new_str)
