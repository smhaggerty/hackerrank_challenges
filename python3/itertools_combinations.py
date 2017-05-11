from itertools import combinations
s, k = input().split()
for i in range(1,int(k)+1):
    print(*sorted(map(lambda x:''.join(x),combinations(sorted(s),i))),sep='\n')
