"""6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число."""

from random import randint


a = randint(0, 100)
i = 0
while i < 10:
    x = int(input(': '))
    if x == a:
        print('Вы выиграли!')
        break
    if x > a:
        print(f"Вы ввели слишком большое число \nУ вас осталось {9-i} попыток")
    if x < a:
        print(f"Вы ввели слишком маленькое число \nУ вас осталось {9-i} попыток")
    i += 1
else:
    print(f'Вы проиграли! Число было {a}')