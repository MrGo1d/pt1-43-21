"""
Упорядоченный список.
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
Задачу поместите в файл task6.py в папке src/homework3.
"""


list_of_num = [1, 0, 0, 4, 0, 4, 0, 6]

for i in list_of_num:
    if i == 0:
        list_of_num.remove(i)
        list_of_num.append(i)

print(list_of_num)
