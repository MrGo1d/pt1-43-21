"""
2. List practice
1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента
не было.
"""


from copy import copy

# step#1
lst = [i + j for i in 'ab' for j in 'bcd']
# step#2
lst_slice = lst[::2]
# step#3
lst_num = [str(i) + 'a' for i in range(1, 5)]
# step#4
print(lst_num.pop(1))
# step#5
lst_copy = (copy(lst_num))
lst_copy.append('2a')

