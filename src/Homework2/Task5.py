n = int(input('Введите порядковый номер искомого числа Фибоначчи:\n'))
if n == 1:
    fib_2 = 0
else:
    fib_1 = 0
    fib_2 = 1
    counter = 0
    while counter < n - 2:
        fib = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib
        counter += 1

print(f'Значение числа Фибоначчи с порядковым номером {n}:', fib_2)
