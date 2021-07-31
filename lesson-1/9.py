# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('1: '))
b = int(input('2: '))
c = int(input('3: '))

middle = a
if a < b < c or a > b > c:
    middle = b
elif a < c < b or a > c > b:
    middle = c
print(f'Среднее число из {a, b, c} это {middle}')
