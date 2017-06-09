import re

for i in range(int(input())):
    input_trimmed = ''.join(input().split(':')[1:])
    hex_codes = re.findall('#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}', input_trimmed)
    if hex_codes:
        print(*hex_codes, sep='\n')
