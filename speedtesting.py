import timeit



print("-".join(str(n) for n in range(100)))
print("-".join([str(n) for n in range(100)]))
print("-".join(map(str, range(100))))

a = timeit.timeit("-".join(str(n) for n in range(100)), number=10000)
b = timeit.timeit("-".join([str(n) for n in range(100)]), number=10000)
c = timeit.timeit("-".join(map(str, range(100))), number=10000)

print(a)
print(b)
print(c)


import time
print(time.perf_counter())
print('Some code.')
print(time.perf_counter())