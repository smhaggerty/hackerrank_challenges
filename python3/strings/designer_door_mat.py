h, w = map(int,input().split())
specifier = '{:-^{width}}'
pattern = [specifier.format('.|.' * (i*2 + 1),width=w) for i in range(h // 2)]
pattern = pattern + ['WELCOME'.center(w, '-')] + pattern[::-1]
print(*pattern, sep='\n')
