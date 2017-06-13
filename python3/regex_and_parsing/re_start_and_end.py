import re
s, k = input().strip(), input().strip()
match_string = '(?=(' + k + '))'
matches = [(m.start(), m.end(1) - 1) for m in re.finditer(match_string, s)]

if matches:
    print(*matches, sep='\n')
else:
    print((-1, -1))
