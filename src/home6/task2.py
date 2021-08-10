class TooManyErrors(Exception):
    """Исключение,  возбуждаемое при превышении допускаемого

    количества попыток неправильного ввода
    """

    def __init__(self, text):
        self.text = text
        print(text)


def decor(n):
    """Создайте декоратор, который вызывает задекорированную функцию

    пока она не выполнится без исключений (но не более n раз -
    параметр декоратора). Если превышено количество попыток, должно быть
    возбуждено исключение типа TooManyErrors
    """
    n = int(n)

    def wrap(func1):
        def called(*args, **kwargs):
            nonlocal n
            if n != 0:
                try:
                    return func1(*args, **kwargs)
                except ZeroDivisionError:
                    print('Было введено неверное значение')
                    n -= 1
            else:
                raise TooManyErrors('Максимальное количество'
                                    ' неправильных попыток достигнуто!')

        return called

    return wrap


@decor(2)
def sum(a, b):
    print(int(a / b))


sum(10, 5)
sum(10, 0)
sum(10, 2)
sum(10, 0)
sum(10, 0)
