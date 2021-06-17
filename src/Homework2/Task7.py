side1 = int(input('Введите сторону а:\n'))
side2 = int(input('Введите сторону b:\n'))
side3 = int(input('Введите сторону c:\n'))

if side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1:
    perimeter = (side1 + side2 + side3) / 2
    area_tr = (perimeter * (perimeter - side1) * (perimeter - side2) * (perimeter - side3)) ** 0.5
    print('Это треугольник!\n')
    print('Площадь этого треугольника:', area_tr)
else:
    print('Это не треугольник!')
