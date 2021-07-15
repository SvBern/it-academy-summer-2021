def get_ranges(list1):
    """

    Реализовать функцию get_ranges которая получает на вход
    непустой список неповторяющихся целых чисел,
    отсортированных по возрастанию, которая этот список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
    """
    temp_list = []
    prev_num = 0
    for num in list1:
        if not temp_list:
            temp_list.append([num])
        elif num - prev_num == 1:
            temp_list[-1].append(num)
        else:
            temp_list.append([num])
        prev_num = num
    final_list = []
    for item in temp_list:
        if len(item) > 1:
            final_list.append(str(item[0]) + "-" + str(item[-1]))
        else:
            final_list.append(str(item[0]))
    for i in final_list[0:-1]:
        print(i, end=",")
    print(final_list[-1])


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
