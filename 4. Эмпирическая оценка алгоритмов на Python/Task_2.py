import timeit
import cProfile

LEN = 1000

# Вариант с решетом
def sieve(n):
    array = [i for i in range(LEN)]

    array[1] = 0

    for i in range(2, LEN):
        if array[i] != 0:
            j = i + i
            while j < LEN:
                array[j] = 0
                j += i

    sieved_array = [i for i in array if i != 0]

    return sieved_array[n - 1]

# print(timeit.timeit('sieve(2)', number=1000, globals=globals()))    # 0.4039235
# print(timeit.timeit('sieve(4)', number=1000, globals=globals()))    # 0.49128819999999995
# print(timeit.timeit('sieve(8)', number=1000, globals=globals()))    # 0.4487865000000001
# print(timeit.timeit('sieve(16)', number=1000, globals=globals()))   # 0.5027930999999999
# print(timeit.timeit('sieve(32)', number=1000, globals=globals()))   # 0.37739789999999984
# print(timeit.timeit('sieve(1)', number=1000, globals=globals()))    # 0.3688465999999999
# print(timeit.timeit('sieve(10)', number=1000, globals=globals()))   # 0.41845409999999994
# print(timeit.timeit('sieve(100)', number=1000, globals=globals()))  # 0.35335150000000004

# cProfile.run('sieve(150)')

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 Task_2.py:19(<listcomp>)
   #      1    0.001    0.001    0.001    0.001 Task_2.py:6(sieve)
   #      1    0.000    0.000    0.000    0.000 Task_2.py:8(<listcomp>)
   #      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Без решета

def prime(n):
    array = []
    num = 2
    while len(array) < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            array.append(num)
        num += 1

    return array[n - 1]

# print(timeit.timeit('prime(2)', number=1000, globals=globals()))    # 0.0019122999999999987
# print(timeit.timeit('prime(4)', number=1000, globals=globals()))    # 0.0055388000000000034
# print(timeit.timeit('prime(8)', number=1000, globals=globals()))    # 0.008859500000000006
# print(timeit.timeit('prime(16)', number=1000, globals=globals()))   # 0.0353608
# print(timeit.timeit('prime(32)', number=1000, globals=globals()))   # 0.12383040000000001
# print(timeit.timeit('prime(1)', number=1000, globals=globals()))    # 0.0005663000000000196
# print(timeit.timeit('prime(10)', number=1000, globals=globals()))   # 0.01626330000000001
# print(timeit.timeit('prime(100)', number=1000, globals=globals()))  # 1.9045222

# cProfile.run('prime(150)')
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 Task_2.py:44(prime)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#       863    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       150    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''Выводы:

У алгоритма, написанного через решето эратосфена, константная сложность, а у второго 
алгоритма - квадратичная. Тем не менее, алгоритм с решетом имеет недостаток - мы не можем
наперед знать, сколько натуральных чисел нужно просмотреть, чтобы найти n-е простое число. 
Поэтому, в случае малых номеров n ~ 100, алгоритм с решетом будет работать быстрее.
Если же n >> 100, лучше будет выбрать алгоритм без решета. Он займет много времени,
но гарантированно даст результат.'''