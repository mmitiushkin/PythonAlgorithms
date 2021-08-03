""" 5. В массиве найти максимальный отрицательный элемент.
       Вывести на экран его значение и позицию в массиве."""

import random

lst = [random.randint(-100, 100) for _ in range(10)]
print(lst)

min_index = 0
for i in lst:
    if i < lst[min_index]:
        min_index = lst.index(i)

print(f'Максимальное отрицательное число: {lst[min_index]}\n'
      f'Его позиция: {min_index}')
