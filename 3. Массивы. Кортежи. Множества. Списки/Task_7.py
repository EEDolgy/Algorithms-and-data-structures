import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count_array = {
    'sm': array[0],
    'second_sm': array[1],
    'sm_count': 1
}

for item in array[1:]:
    if item < count_array['sm']:
        count_array['second_sm'] = count_array['sm']
        count_array['sm'] = item
        count_array['sm_count'] = 1
    elif item == count_array['sm']:
        count_array['sm_count'] += 1
    elif item < count_array['second_sm']:
        count_array['second_sm'] = item

if count_array['sm_count'] == 1:
    print(f"Два наименьших элемента - {count_array['sm']} и {count_array['second_sm']}")
else:
    print(f"Два наименьших элемента - {count_array['sm']} и {count_array['sm']}")