import numpy
array_a = [*map(float, input().split())]
methods = [numpy.floor, numpy.ceil, numpy.rint]

for method in methods:
    print(method(array_a))
