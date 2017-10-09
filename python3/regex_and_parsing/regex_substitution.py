import re

string_list = [input() for i in range(int(input()))]

for string in string_list:
    string = re.sub(r'(?<=\s)\&\&\s', 'and ', string)
    string = re.sub(r'(?<=\s)\|\|\s', 'or ', string)
    print(string)