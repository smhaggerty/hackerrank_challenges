import re
column_height, row_length = input().split()
rows = [input() for _ in range(int(column_height))]
string = str()
for i in range(int(row_length)):
    for j in range(int(column_height)):
        string += rows[j][i]
print(re.sub(r'(?<=\w)\W+(?=\w)', ' ',string))
