# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

a = int(input('Введите год: '))

if a % 4 == 0:
    print(f'Год {a} является високосным')
else:
    print(f'Год {a} является невисокосным')
