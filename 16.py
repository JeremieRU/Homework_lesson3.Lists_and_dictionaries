# 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве a[1..N]. Пользователь 
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках 
# записаны N целых чисел ai. Последняя строка содержит число X

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

n = int(input("Введите количество элементов в массиве: "))

array = []

minarr = int(input("Введите нижний порог значений массива: "))
maxarr = int(input("Введите верхний порог значений массива: "))

for i in range(1,n+1):
    array.append(random.randint(minarr, maxarr))

x = int(input("Введите искомое число: "))
count = 0

print(array)

for i in array:
    if i == x:
        count += 1

print(f"Элемент {x} встречается в массиве {count} раз.")