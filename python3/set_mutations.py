# take in input
_, a, n  = int(input()), set(input()), int(input())
operation_and_set = [input() for i in range(2 * n)]
# remove whitespace from set and convert elements to integers
a.remove(' ')
a = set(map(int, a))
# loop through operations and
for i in range(0, n * 2, 2):
    operation = operation_and_set[i].split()[0]
    active_set = set(map(int, set(operation_and_set[i + 1].split())))
    eval('a.' + operation + '(active_set)')
print(sum(a))
