from itertools import combinations_with_replacement as cwr
s, k = input().split()
print(*map(lambda x:''.join(x),cwr(sorted(s),int(k))),sep="\n")
