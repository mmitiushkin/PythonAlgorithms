# 4. Определить, какое число в массиве встречается чаще всего.

import random

lst = [random.randint(0, 100) for _ in range(100)]
print(lst)

max_index = 0
b = 0
for i in lst:
    b = lst.count(lst[max_index])
    if lst.count(i) > b:
        max_index = lst.index(i)

print(f'Число {lst[max_index]} встречается {b} раз(a)')
