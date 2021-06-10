L = input('Сколько наименований товара вы покупаете?\n')
L = int(L)

i = 1
SUM = 0
M = 0
N = 0
while i <= L:
    print('Сколько вы покупаете товара', + i)
    s = int(input())
    print('Введите стоимость за единицу товара', + i)
    print('рублей')
    M = int(input())
    print('копеек')
    N = int(input())
    coins = M*100 + N
    sum = 0
    sum = sum + coins * s
    M = sum // 100
    N = sum % 100
    print('Итого за данный товар', + M, 'руб.', + N, 'коп.')
    SUM = SUM + sum
    M = SUM // 100
    N = SUM % 100
    i = i + 1

print('Общая сумма покупки', + M, 'руб', + N, 'коп')
