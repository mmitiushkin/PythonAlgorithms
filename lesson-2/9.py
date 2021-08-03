"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""

x = [i for i in input(': ').split()]


def f(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum


max_sum = 0
max_num = 0

for i in x:
    if f(i) > max_sum:
        max_num = i
        max_sum = f(i)

print(f'Сумма цифр числа {max_num} = {max_sum}')