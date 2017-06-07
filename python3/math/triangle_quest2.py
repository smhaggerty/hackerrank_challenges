for i in range(1,int(input())+1):
	print(sum(map(lambda x: 1 * (10 ** x) , range(i))) ** 2)
# the trick is recognizing that the numbers are demlo numbers, which are the
# squares of the sequence of base 10 repunits.
