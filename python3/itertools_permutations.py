from itertools import permutations
s, k = input().split()
print(*map(lambda x: ''.join(x), sorted(permutations(s,int(k)))),sep="\n")
