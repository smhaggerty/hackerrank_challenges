import numpy
n, m, p = map(int, input().split())

array_n = numpy.array([list(map(int,input().split())) for i in range(n)])
array_p = numpy.array([list(map(int,input().split())) for i in range(m)])

print(numpy.concatenate((array_n, array_p)))
