import numpy
n = int(input())
determinant = numpy.linalg.det([list(map(float, input().split())) for i in range(n)])
print(determinant)
