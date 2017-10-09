import re

match_string = r'(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}[aeiouAEIOU]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}))'

matches = re.findall(match_string, input())

if matches != []:
    for match in matches:
        print(match[1:-1])
else:
    print(-1)