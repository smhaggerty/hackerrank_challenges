import numpy
n, _ = map(int, input().split())

array_a = [list(map(int, input().split())) for i in range(n)]
array_b = [list(map(int, input().split())) for i in range(n)]
methods = [numpy.add, numpy.subtract, numpy.multiply, numpy.divide, numpy.mod, numpy.power]

for method in methods:
    print(method(array_a, array_b).astype(int))
