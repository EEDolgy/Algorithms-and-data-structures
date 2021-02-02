'''Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры'''

import timeit
import cProfile

# 1. Вариант (точно знаем что функция дает верные результаты)
def sum_rec_mem(n):
    if n == 0:
        return 1
    return sum_rec_mem(n - 1) + pow((-0.5), n)

# print(timeit.timeit('sum_rec_mem(2)', number=10000, globals=globals()))   # 0.006319199999999997
# print(timeit.timeit('sum_rec_mem(4)', number=10000, globals=globals()))   # 0.016364200000000002
# print(timeit.timeit('sum_rec_mem(8)', number=10000, globals=globals()))   # 0.03303310000000001
# print(timeit.timeit('sum_rec_mem(16)', number=10000, globals=globals()))  # 0.0689137
# print(timeit.timeit('sum_rec_mem(32)', number=10000, globals=globals()))  # 0.1437321
# print(timeit.timeit('sum_rec_mem(64)', number=10000, globals=globals()))  # 0.28824110000000003
#
# cProfile.run('sum_rec_mem(990)') # Вызывается 991 раз, все вызовы в сумме происходят за 0.001 сек.

# Проверка

def test_sum(func):
    k = 10
    for i in range(1, k):
        assert  func(i) == sum_rec_mem(i), f'Ошибка для {i=}'
        print('Test OK')

# 2. Вариант

def sum_cyc(n):
    sum_ = 0
    for i in range(n + 1):
        sum_ += pow((-0.5), i)
    return sum_

# test_sum(sum_cyc)

# print(timeit.timeit('sum_cyc(2)', number=10000, globals=globals()))     # 0.010976600000000003
# print(timeit.timeit('sum_cyc(4)', number=10000, globals=globals()))     # 0.014893699999999996
# print(timeit.timeit('sum_cyc(8)', number=10000, globals=globals()))     # 0.02416760000000001
# print(timeit.timeit('sum_cyc(16)', number=10000, globals=globals()))    # 0.042031799999999994
# print(timeit.timeit('sum_cyc(32)', number=10000, globals=globals()))    # 0.076154
# print(timeit.timeit('sum_cyc(64)', number=10000, globals=globals()))    # 0.1528067
# print(timeit.timeit('sum_cyc(1)', number=10000, globals=globals()))     # 0.0067554000000000225
# print(timeit.timeit('sum_cyc(10)', number=10000, globals=globals()))    # 0.029554099999999972
# print(timeit.timeit('sum_cyc(100)', number=10000, globals=globals()))   # 0.2989131
# print(timeit.timeit('sum_cyc(1000)', number=10000, globals=globals()))  # 2.5205271000000002

# cProfile.run('sum_cyc(1_000_000)')

  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.000    0.000    0.478    0.478 <string>:1(<module>)
  #       1    0.170    0.170    0.478    0.478 Task_1.py:33(sum_cyc)
  #       1    0.000    0.000    0.478    0.478 {built-in method builtins.exec}
  # 1000001    0.309    0.000    0.309    0.000 {built-in method builtins.pow}
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 3. Вариант

def sum_formula(n):
    n = n + 1
    return (1 - pow((-0.5), n)) / (1 - (-0.5))

# test_sum(sum_formula)

# print(timeit.timeit('sum_formula(2)', number=10000, globals=globals()))     # 0.004049200000000003
# print(timeit.timeit('sum_formula(4)', number=10000, globals=globals()))     # 0.0037934000000000023
# print(timeit.timeit('sum_formula(8)', number=10000, globals=globals()))     # 0.003567600000000004
# print(timeit.timeit('sum_formula(16)', number=10000, globals=globals()))    # 0.0044389000000000026
# print(timeit.timeit('sum_formula(32)', number=10000, globals=globals()))    # 0.0035902000000000017
# print(timeit.timeit('sum_formula(64)', number=10000, globals=globals()))    # 0.003528500000000004
# print(timeit.timeit('sum_formula(1)', number=10000, globals=globals()))     # 0.003188399999999994
# print(timeit.timeit('sum_formula(10)', number=10000, globals=globals()))    # 0.0033474000000000004
# print(timeit.timeit('sum_formula(100)', number=10000, globals=globals()))   # 0.0035150999999999932
# print(timeit.timeit('sum_formula(1000)', number=10000, globals=globals()))  # 0.0037389000000000033
#
# cProfile.run('sum_formula(1_000_000)')
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_1.py:63(sum_formula)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''Выводы:

1) В вариантах 1 и 2 прослеживается линейная зависимость от времени O(N), 
в 3 варианте - зависимости нет (т.е. константное время O(1)). Во всех случаях это
совпадает с ожидаемыми зависимостями

2) Вариант 2, выполненный без рекурсии, совпадает по сложности с первым, 
но дает больше возможностей (не нужно учитывать глубину рекурсии), поэтому на малых n < 1000
в плане затрат времени оба варианта эквивалентны. Но при работе с большими данным стоит 
использовать вариант без рекурсии

3) Глобально наиболее выигрышный 3-й вариант
'''