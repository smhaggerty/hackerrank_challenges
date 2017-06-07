import numpy
input_parameters = tuple(map(int, input().split()))

array_of_zeros = numpy.zeros(input_parameters, int)
array_of_ones = numpy.ones(input_parameters, int)

print(array_of_zeros, array_of_ones, sep='\n')
