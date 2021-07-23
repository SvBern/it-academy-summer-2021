"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули,
getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name..
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
import homework2
import homework3
import homework4

from inspect import getmembers
from inspect import isfunction

list_func2 = [elem[0] for elem in getmembers(homework2) if isfunction(elem[1])]
list_func3 = [elem[0] for elem in getmembers(homework3) if isfunction(elem[1])]
list_func4 = [elem[0] for elem in getmembers(homework4) if isfunction(elem[1])]


def runner(*args):
    if not args:
        print('Будут выполнены все функции по порядку: ')
        for func in list_func2:
            call_def = getattr(homework2, func)
            call_def()
        for func in list_func3:
            call_def = getattr(homework3, func)
            call_def()
        for func in list_func4:
            call_def = getattr(homework4, func)
            call_def()
    else:
        for func in args:
            if func in list_func2:
                call_def = getattr(homework2, func)
                call_def()
            elif func in list_func3:
                call_def = getattr(homework3, func)
                call_def()
            elif func in list_func4:
                call_def = getattr(homework4, func)
                call_def()


runner('check_country', 'couple_of_element')
