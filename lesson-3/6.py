"""6. В одномерном массиве найти сумму элементов,
      находящихся между минимальным и максимальным элементами.
      Сами минимальный и максимальный элементы в сумму не включать."""
import random

lst = [random.randint(0, 100) for _ in range(10)]
print(lst)

a = max(lst)
b = min(lst)
a_id = lst.index(a)
b_id = lst.index(b)
if b_id < a_id:
    new_lst = lst[b_id+1:a_id]
else:
    new_lst = lst[a_id+1:b_id]

print(new_lst)
print(sum(new_lst))
