# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
import timeit


def func1(x):
    return str(x)[::-1]


def func2(x):
    m = 0
    while x > 0:
        m = m*10 + x%10
        x = x // 10
    return m


"""
Сложность обоих функций равна n
О(n)=n
"""


time1 = timeit.timeit('func1(1234)',
                      setup='from __main__ import func1',
                      number=10)

time2 = timeit.timeit('func2(1234)',
                      setup='from __main__ import func2',
                      number=10)

print(f'time func1 = {time1}')
print(f'time func2 = {time2}')
print(f'Разница = {round(time1 / time2, 2)}')

"""
1).
time func1 = 1.7299999999997873e-05
time func2 = 1.0200000000001874e-05
Разница = 1.7

2).
time func1 = 9.599999999998499e-06
time func2 = 9.900000000000186e-06
Разница = 0.97

3).
time func1 = 1.1099999999999999e-05
time func2 = 1.1000000000004062e-05
Разница = 1.01
"""