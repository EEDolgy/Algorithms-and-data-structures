import random

M = 5
SIZE = 2 * M + 1
FST = 0
LST = 100

def median(arr):
    ls = 0
    gt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[j] < arr[i]:
                    ls += 1
                else:
                    gt += 1
        if gt == ls:
            return arr[i]
        ls = 0
        eq = 0
        gt = 0

array = [random.randint(FST, LST) for _ in range(SIZE)]

print(array)
print(f'Медиана равна {median(array)}')
