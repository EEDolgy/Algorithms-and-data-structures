'''Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр'''

def summ(n):
    if n // 10 == 0:
        return n
    return n % 10 + summ(n // 10)

sum = 0

n = int(input('Введите натуральное число или 0 чтобы закончить ввод: '))

while n != 0:
    s = summ(n)
    if s > sum:
        sum = s
        num = n
    n = int(input())

print(f'Число с наибольшей суммой цифр {num}, '
          f'\nсумма его цифр равна {sum}')