import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

array2 = []

for i, item in enumerate(array):
    if item % 2 == 0:
        array2.append(i)

print(array, array2, sep = '\n')