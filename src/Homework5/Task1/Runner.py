"""

Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули,
getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
import Homework2
import Homework3
import Homework4


def runner(*args, **kwargs):
    if not args and kwargs:
        print('Будут выполнены все функции по порядку: ')
        Homework2.count_cost_goods()
        Homework2.more_long_word()
        Homework2.deleting_repeats()
        Homework2.counter_letters()
        Homework2.fibonacci()
        Homework2.palindrome()
        Homework2.area_of_a_triangle()
        Homework2.numbers()
        Homework2.middle_of_a_word()
        Homework2.determine_the_century()
        Homework2.isogram()
        Homework2.logo()
        Homework3.sorting_numbers()
        Homework3.output_numbers()
        Homework3.unique_elements()
        Homework3.couple_of_element()
        Homework3.fizz_buzz()
        Homework3.value_of_var()
        Homework3.do_tuple_and_list()
        Homework3.do_list_and_tuple()
        Homework3.num_letter()
        Homework3.addition_of_letters()
        Homework3.copy_list()
        Homework3.cut_element()
        Homework3.cut_syllables()
        Homework4.do_list_of_languages()
        Homework4.euclidean_algorithm()
        Homework4.count_diff_num()
        Homework4.diff_words()
        Homework4.cubed_of_num()
        Homework4.diff_num_in_one()
        Homework4.check_country()
    else:
        for arg in args:
            return arg
        for kwarg in kwargs:
            return kwarg


runner(Homework4.diff_words())
runner(func1=Homework4.check_country(), func2=Homework4.diff_num_in_one())
runner()
