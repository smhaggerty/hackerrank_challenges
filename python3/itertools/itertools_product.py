from itertools import product
a, b = map(int, input().split()), map(int, input().split())
print(*product(a,b))
