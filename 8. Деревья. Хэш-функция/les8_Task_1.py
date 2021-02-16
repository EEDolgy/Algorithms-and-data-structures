'''Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.'''

str_ = input('Введите строку текста: ')
count = 1
hash_list = []

for i in range(len(str_)):
    for j in range(i + 1, len(str_) + 1):
        spam = str_[i:j]
        eggs = hash(spam)
        if eggs not in hash_list:
            hash_list.append(eggs)
            count += 1

print(f'Number of distinct substrings is {count}')