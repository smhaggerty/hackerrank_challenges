import numpy
rows, columns, number_of_nested_arrays = map(int, input().split())

array_of_zeros = numpy.zeros((rows, columns, number_of_nested_arrays), dtype=int)
array_of_ones = numpy.ones((rows, columns, number_of_nested_arrays), dtype=int)

print(array_of_zeros)
print(array_of_ones)
