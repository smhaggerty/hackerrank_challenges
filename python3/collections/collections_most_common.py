from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
     pass

string = input()

#find the top three,
top_three = OrderedCounter(sorted(string)).most_common(3)
print(*['{0} {1}'.format(i[0], i[1]) for i in top_three], sep='\n')
