str1 = input('Введите предложение\n')
long_word = max(str1.split(), key = len)
print("Самое длинное слово в предложении: ", long_word)
