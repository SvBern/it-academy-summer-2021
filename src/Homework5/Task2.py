def storage_of_results_decor(func):
    """Создайте декоратор,

    который хранит результаты вызовов функции
    (за все время вызовов, не только текущий запуск программы)
    """
    list_results = []

    def wrapper(*args, **kwargs):
        nonlocal list_results
        result = func(*args, **kwargs)
        list_results.append(result)
        print('Результат хранения: ', list_results)
        return result

    return wrapper
