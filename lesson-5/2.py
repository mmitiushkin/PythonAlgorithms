"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""
from collections import deque


nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def plus(a, b):
    if a > b:
        a, b = b, a

    b = b[::-1]
    a = deque(a)
    b = deque(b)
    res_plus = []

    j = -1
    k = 0
    for i in b:
        first = nums[i]
        second = nums[a[j]]
        r_plus = (first + second + k) % 16
        for key, value in nums.items():
            if value == r_plus:
                res_plus.append(key)
        if first + second > 15:
            k = 1
        else:
            k = 0
        j -= 1
        if j == -len(a) - 1:
            break

    b = list(b)
    diff = len(b) - len(a)
    if diff:
        for i in b[-diff:]:
            r = nums[b[-diff]] + k
            for key, value in nums.items():
                if value == r:
                    res_plus.append(key)

    if k == 1:
        res_plus.append(1)

    return res_plus[::-1]


def mult(a, b):
    if a < b:
        a, b = b, a

    b = b[::-1]
    a = a[::-1]
    a = deque(a)
    b = deque(b)
    x = []
    for i in b:
        y = []
        k = 0
        for j in a:
            first = nums[i]
            second = nums[j]
            r = (first * second + k) % 16
            for key, value in nums.items():
                if value == r:
                    y.append(key)
            if first * second + k > 15:
                k = (first * second + k) // 16
            else:
                k = 0
        y.append(f'{k}')
        x.append(y[::-1])
    x[1].append('0')
    x1 = ''.join(x[0])
    x2 = ''.join(x[1])

    return plus(x1, x2)


a = 'A2'
b = 'C4F'

print(f'Сумма чисел {a} и {b} = {plus(a, b)}')
print(f'Сумма чисел {a} и {b} = {mult(a, b)}')

