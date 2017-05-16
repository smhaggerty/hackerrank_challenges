from collections import OrderedDict
n = int(input())
itemsAndPrices = [input().split() for i in range(n)]
orderedDict = OrderedDict()
for item in itemsAndPrices:
    key = ' '.join(item[:-1])
    orderedDict[key] = orderedDict.get(key,0) + int(item[-1])
for key, value in orderedDict.items():
    print('{} {}'.format(key, str(value)))
