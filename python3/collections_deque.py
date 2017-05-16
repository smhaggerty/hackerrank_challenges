from collections import deque
d = deque()
n = int(input())
methodsAndInput = [input().split() for i in range(n)]
for i in range(n):
        getattr(d, str(methodsAndInput[i][0]))(*methodsAndInput[i][1] if len(methodsAndInput[i]) > 1 else [])
print(*d)
