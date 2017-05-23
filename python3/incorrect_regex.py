import re
cases = [input() for i in range(int(input()))]
for case in cases:
    try:
        re.compile(case)
        print(True)
    except:
        print(False)
