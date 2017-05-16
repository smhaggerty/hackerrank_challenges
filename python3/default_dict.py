from collections import defaultdict
n, m = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for i in range(m)]
defaultDict = defaultdict(list)

for i, word in enumerate(a):
    defaultDict[word].append(i+1)

for word in b:
    if word in defaultDict:
        print(*defaultDict[word])
    else: print(-1)
