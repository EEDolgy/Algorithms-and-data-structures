from  collections import defaultdict

n = int(input('Введите количество компаний: '))

companies = defaultdict(float)

for _ in range(n):
    comp = input('Введите название компании: ')
    for i in range(1, 5):
        income = float(input(f'Введите прибыль за {i} квартал: '))
        companies[comp] += income

avg_inc = 0

for item in companies.values():
    avg_inc += item

avg_inc /= len(companies)

print(f'Средняя прибыль для всех предприятий равна: {avg_inc}')
print('Предприятия, прибыль которых ниже средней: ')
for key, val in companies.items():
    if val < avg_inc:
        print(key, end=' ')
print('\nПредприятия, прибыль которых выше средней: ')
for key, val in companies.items():
    if val > avg_inc:
        print(key, end=' ')