import re
s = input()
m = re.search(r'([\dA-Za-z])\1', s)
if m != None:
    print(m.group(1))
else:
    print(-1)
