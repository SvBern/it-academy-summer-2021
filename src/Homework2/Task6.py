n = int(input('Введите число:\n'))

temporarily = n
reverse = 0
while n > 0:
    rest = n % 10
    reverse = reverse * 10 + rest
    n = n // 10
if reverse == temporarily:
    print('Это число - палиндром!')
else:
    print('Это не палиндром!')
