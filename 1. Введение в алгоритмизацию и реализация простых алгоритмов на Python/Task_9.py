'''Вводятся три разных числа. Найти, какое из них
является средним (больше одного, но меньше другого).'''

print('Введите три различных числа')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if (a < b < c) or (c < b < a):
    print(f'Среднее число - {b}')
elif (b < a < c) or (c < a < b):
    print(f'Среднее число - {a}')
else:
    print(f'Среднее число - {c}')

