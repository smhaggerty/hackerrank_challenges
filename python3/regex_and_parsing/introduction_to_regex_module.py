import re
test_cases = [input() for _ in range(int(input()))]
for case in test_cases:
    print(bool(re.match('^[+-]?\d*\.\d+$', case)))
