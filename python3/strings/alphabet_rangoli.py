def print_rangoli(size):
    width = size * 4 - 3
    alphabet = [chr(97 + i) for i in range(size)]
    rows = ['-'.join(alphabet[-1::-1] + alphabet[1:])]

    for i in range(size - 1):
        letters = alphabet[-1:i+1:-1] + alphabet[i+1:]
        row = '{:-^{width}}'.format('-'.join(letters),width=width)
        rows.append(row)
        rows.insert(0, row)

    print(*rows, sep='\n')
