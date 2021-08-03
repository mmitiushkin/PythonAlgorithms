# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

n = 5
a = []
for i in range(n):
    b = []
    for j in range(5):
        b.append(randint(0, 10))
        print(f'{b[j]:2}', end=' ')
    a.append(b)
    print()

min_lst = []
for i in range(n):
    s = []
    for j in range(n):
        s.append(a[j][i])
    min_lst.append(min(s))


print(f"Максимальный элемент среди минимальных элементов столбцов матрицы - {max(min_lst)}")

