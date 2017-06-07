from itertools import product
k, m = map(int, input().split())
lists = [map(int, input().split()[1:]) for i in range(k)]
# evaluate the equation for each group of x values then print the max
print(max([sum(map(lambda x: x**2, combo)) % m for combo in product(*lists)]))
