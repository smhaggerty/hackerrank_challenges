import re
# valid phone numbers are 10 digit numbers beginning with 7, 8, 9
for i in range(int(input())):
    if re.fullmatch('[789][0-9]{9}', input()):
        print('YES')
    else:
        print('NO')
