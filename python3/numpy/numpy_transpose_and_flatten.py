import numpy
n, m = map(int, input().split(' '))
array = numpy.array([list(map(int, input().split(' '))) for i in range(n)])
print(numpy.transpose(array), array.flatten(), sep='\n')
