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

for i in range(n):
    print(f'--', end=' ')
print()

for i in range(n):
    s = 0
    for j in range(n):
        s += a[j][i]
    print(s, end=' ')

