"""3. В массиве случайных целых чисел
      поменять местами минимальный и максимальный элементы."""
from random import randint

lst = [randint(0, 10) for i in range(10)]

max_int = max(lst)
min_int = min(lst)

max_id = lst.index(max_int)
min_id = lst.index(min_int)

print(lst)
print()

max_id, min_id = min_id, max_id
lst[max_id] = max_int
lst[min_id] = min_int

print(lst)
