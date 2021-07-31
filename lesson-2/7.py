"""7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число."""

x = int(input(': '))


def f1(n):
    if n == 0:
        return 0
    while n > 0:
        return n + f1(n-1)


def f2(n):
    return n*(n+1)//2


for i in range(100):
    if f1(i) == f2(i):
        print(f'Для n={i} - True')
    else:
        print(f'Для n={i} - False')