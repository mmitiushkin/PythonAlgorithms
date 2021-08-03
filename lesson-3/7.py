"""7. В одномерном массиве целых чисел определить два наименьших элемента.
      Они могут быть как равны между собой (оба являться минимальными), так и различаться."""
import random

lst = [random.randint(0, 100) for _ in range(10)]
print(lst)

new_lst = [min(lst)]
lst.remove(min(lst))
new_lst.append(min(lst))

print(new_lst)
