str1 = input('Введите любую строку латиницей\n')

low_letter = 0
up_letter = 0
for element in str1:
    if 'a' <= element <= 'z':
        low_letter += 1
    if 'A' <= element <= 'Z':
        up_letter += 1

print('Количество строчных букв:', low_letter)
print('Количество прописных букв:', up_letter)
