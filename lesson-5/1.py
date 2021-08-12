"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего. """
import collections

Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])
a = int(input(": "))
b = {}
c = {}

for i in range(a):
    name = input(f"Название для {i+1}: ")
    q1 = int(input(f"1 для {name}: "))
    q2 = int(input(f"2 для {name}: "))
    q3 = int(input(f"3 для {name}: "))
    q4 = int(input(f"4 для {name}: "))
    b[name] = Enterprise(
        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4
    )
    c[name] = sum(b[name])//len(b[name])


total = sum(c.values()) // len(c.values())
print(f'Средняя прибыль: {total}')

higher = []
lower = []
for i in c:
    if c[i] > total:
        higher.append(i)
    else:
        lower.append(i)

print(f'higher: {higher}')
print(f'lower: {lower}')

