from itertools import groupby
s = input()
print(*[(len(list(g)), k) for k, g in groupby(s, int)])
