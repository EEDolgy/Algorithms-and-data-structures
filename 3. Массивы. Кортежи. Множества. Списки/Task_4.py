import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count_dict = dict()

for item in array:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

max = 0

for item in count_dict.values():
    if max < item:
        max = item

for i, item in count_dict.items():
    if item == max:
        print(f'Чаще всего встречается число {i} - {item} раз.')