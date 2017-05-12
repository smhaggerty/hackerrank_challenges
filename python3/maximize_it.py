from itertools import product
k, m = map(int, input().split())
# store lists as sets because ordering/repeats don't matter within each list
lists = [set(map(int, input().split()[1:])) for i in range(k)]
# evaluate the equation for each group of x values then print the max
print(max([sum(map(lambda x: x**2, combo)) % m for combo in product(*lists)]))
