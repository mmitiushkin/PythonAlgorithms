"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»"""
import timeit


def withoutE(i):
    prime_nums = [2]
    m = 3
    while len(prime_nums) < i:
        for j in prime_nums:
            if m % j == 0:
                break
        else:
            prime_nums.append(m)
        m += 1
    return prime_nums[-1]


def withE(n, i):
    prime_nums = [j for j in range(2, n+1)]
    for p in prime_nums:
        for j in range(2*p, n+1, p):
            if j in prime_nums:
                prime_nums.remove(j)
    return prime_nums[i-1]


print(withoutE(10))
print(withE(100, 10))

NUMBER_EXECUTIONS = 10

time1 = timeit.timeit('withoutE(10)',
                      setup='from __main__ import withoutE',
                      number=10)

time2 = timeit.timeit('withE(100, 10)',
                      setup='from __main__ import withE',
                      number=10)

print(f'time withoutE = {time1}')
print(f'time withE = {time2}')
print(f'Разница = {round(time1 / time2, 2)}')

"""
time withoutE = 0.00010090000000000099
time withE = 0.0015816000000000024
Разница = 0.06
"""
