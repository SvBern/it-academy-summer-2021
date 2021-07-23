def storage_of_results_decor(func):
    """Создайте декоратор,
    который хранит результаты вызовов функции
    (за все время вызовов, не только текущий запуск программы)
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("all_results.txt", "a") as all_results:
            all_results.write(str(result) + "\n")
        return result

    return wrapper
