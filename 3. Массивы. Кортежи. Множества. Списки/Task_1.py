array = [i for i in range(2, 100)]
array_little = [i for i in range(2, 10)]

LEN_ARRAY_LITTLE = len(array_little)

array_answ = [0] * LEN_ARRAY_LITTLE

for item in array:
    for i in range(0, LEN_ARRAY_LITTLE):
        if item % array_little[i] == 0:
            array_answ[i] += 1

for i in range(0, LEN_ARRAY_LITTLE):
    print(f'В массиве [2..9] {array_answ[i]} чисел, делящихся на {array_little[i]}')
