"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы. """
import random


def merge_sort(x):
    if len(x) < 2:
        return x
    mid = len(x) // 2
    left = merge_sort(x[:mid])
    right = merge_sort(x[mid:])

    i = j = k = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            x[k] = left[i]
            i += 1
        else:
            x[k] = right[j]
            j += 1
        k += 1

    while len(left) > i:
        x[k] = left[i]
        i += 1
        k += 1

    while len(right) > j:
        x[k] = right[j]
        j += 1
        k += 1

    return x


array = [random.uniform(0, 50) for i in range(10)]

print(array)
print(merge_sort(array))
