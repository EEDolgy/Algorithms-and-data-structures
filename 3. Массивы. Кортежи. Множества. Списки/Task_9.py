import random

SIZE_N = 10
SIZE_M = 8
MIN_ITEM = 0
MAX_ITEM = 100
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]

min_col = [array[0][0]] * len(array[0])

for row in array:
    for i, item in enumerate(row):
        print(f'{item:>4}', end = '')
        if item < min_col[i]:
            min_col[i] = item
    print(sep = '\n')

max = min_col[0]

for item in min_col[1:]:
    if item > max:
        max = item

print(f'Минимальные элементы по колонкам: {min_col}')
print(f'Максимальный элемент среди минимальных по колонкам - это {max}')