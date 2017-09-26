import itertools
import timeit

def test(n):
    start_time = timeit.default_timer()
    for i in itertools.permutations(i for i in range(n)):
        pass
    total_time = timeit.default_timer() - start_time
    print("Para {1} elementos, tardó en segundos: {0:.8f}".format(total_time, n))

for i in range(12):
    test(i)
pass
pass
pass