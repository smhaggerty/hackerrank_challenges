import numpy
n = int(input().split()[0])
array = [list(map(int, input().split())) for i in range(n)]

print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(numpy.std(array, axis=None))
