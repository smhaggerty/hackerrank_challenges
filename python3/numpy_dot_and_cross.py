import numpy
n = int(input())
array_a = [list(map(int, input().split())) for i in range(n)]
array_b = [list(map(int, input().split())) for i in range(n)]

print(numpy.dot(array_a, array_b))
