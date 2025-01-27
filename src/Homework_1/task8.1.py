"""Открытая задача:
8. Зарегистрируйтесь на одном (или нескольких) из сайтов:
https://py.checkio.org/ , https://www.codewars.com, https://www.hackerrank.com/,
https://acmp.ru И решите 1-5 задач уровня Elementary и advanced. Поместите 3 простых
и 2 сложных задачи на Ваш выбор в пул реквест.
Эти задачи поместите в файл task8.py в папке src/homework2."""
# задачи решал на codewar

"""Pete likes to bake some cakes. He has some recipes and ingredients.
Unfortunately he is not good in maths. Can you help him to find out, how many
cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients
(also an object) and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are
simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 0, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100},
{sugar: 500, flour: 2000, milk: 2000})
https://www.codewars.com/kata/525c65e51bf619685c000059"""


def cakes(recipe, available):
    result = []
    try:
        for i in recipe:
            result.append(available[i] // recipe[i])
    except ZeroDivisionError:
        result.append(0)
    return min(result)


print(cakes({'flour': 0, 'sugar': 200, 'eggs': 1},
            {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
