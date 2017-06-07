key = lambda x: (x.isdecimal() and int(x)%2 == 0, x.isdecimal(), x.isupper(), x)
print(*sorted(input(), key= key), sep='')
