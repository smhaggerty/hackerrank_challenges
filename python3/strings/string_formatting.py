def print_formatted(number):
    width = len(bin(number)) - 2
    format_string = '{0:>{width}} {0:>{width}o} {0:>{width}X} {0:>{width}b}'
    for i in range(1, number+1):
        print(format_string.format(i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
