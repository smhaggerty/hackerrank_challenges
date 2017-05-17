x, k, p = *map(int, input().split()), input()
if eval(p.replace('x',str(x))) == k:
    print(True)
else:
    print(False)
