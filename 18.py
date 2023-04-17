# 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов
# в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
import math

n = int(input("Введите количество элементов в массиве: "))

array = []

minarr = int(input("Введите нижний порог значений массива: "))
maxarr = int(input("Введите верхний порог значений массива: "))

x = int(input("Введите число, к которому будем искать самый близкий элемент: "))

for i in range(n):
    array.append(random.randint(minarr, maxarr))

result = array[0]
eps = x

for i in array:
    if abs(i - x) < eps:
        eps = abs(i - x)
        result = i

print(array)

print(result)