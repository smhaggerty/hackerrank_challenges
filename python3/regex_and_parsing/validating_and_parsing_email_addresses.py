import re

for i in range(int(input())):
    address = input().split()
    match_string = '<[a-zA-Z][\w.-]+@[a-zA-Z]+[.][a-z]{1,3}>'

    if re.match(match_string, address[1]):
        print(' '.join(address))
