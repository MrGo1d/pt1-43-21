"""
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых
чисел, отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
Задачу поместите в файл task3.py в папке src/homework7
"""


def get_ranges(num_list):
    total = []
    list_tmp = []

    for i in range(len(num_list) - 1):
        if num_list[i] + 1 == num_list[i + 1]:
            list_tmp.append(num_list[i])
        else:
            list_tmp.append(num_list[i])
            total.append(list_tmp)
            list_tmp = []
        if i == len(num_list) - 2:
            if num_list[i] + 1 == num_list[i + 1]:
                if num_list[i] in list_tmp:
                    list_tmp.append(num_list[-1])
                    total.append(list_tmp)
            else:
                list_tmp.append(num_list[-1])
                total.append(list_tmp)

    print(*[str(i[0]) + '-' + str(i[-1]) if len(i) > 1 else str(i[-1]) for i in total], sep=',')


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])