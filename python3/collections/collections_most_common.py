from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

string = input()



#find the top three,
top_three = OrderedCounter(sorted(string)).most_common(3)
print(*['{0} {1}'.format(i[0], i[1]) for i in top_three], sep='\n')
