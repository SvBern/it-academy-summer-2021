L = int(input('Сколько наименований товара вы покупаете?\n'))

counter = 1
SUMMA = 0
M = 0
N = 0
while counter <= L:
    quantity = int(input(f'Какое количество товара {counter} Вы покупаете:\n'))
    print(f'Введите стоимость за единицу товара {counter}')
    M = int(input('рублей:\n'))
    N = int(input('копеек:\n'))
    coins = M * 100 + N
    summa = 0
    summa += coins * quantity
    M = summa // 100
    N = summa % 100
    print('Итого за данный товар:', M, 'руб.', N, 'коп.')
    SUMMA += summa
    M = SUMMA // 100
    N = SUMMA % 100
    counter += 1

print('Общая сумма покупки:', M, 'руб', N, 'коп')
