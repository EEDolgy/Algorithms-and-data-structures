'''https://drive.google.com/file/d/1SYrDuGULpV1j62YbH1TX7FtunTq0ELMc/view?usp=sharing

Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
'''

num = int(input("Введите целое положительное трехзначное число: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum = a + b + c
mult = a * b * c

print(f'Сумма и произведение цифр введенного числа равны: {sum} и {mult}')