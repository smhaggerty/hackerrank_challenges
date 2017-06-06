import numpy
n, _ = map(int, input().split())
array = [list(map(int, input().split())) for i in range(n)]

print(numpy.max(numpy.min(array, axis=1)))
