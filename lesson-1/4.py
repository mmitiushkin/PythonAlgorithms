# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
from random import randint, uniform

a = float(input('1: '))
b = float(input('2: '))
char1 = input('char1 = ').lower()
char2 = input('char1 = ').lower()

print(randint(a, b))
print(uniform(a, b))
print(chr(randint(ord(char1), ord(char2))).lower())
