import itertools
n, elements, k = float(input()), input().split(), int(input())
num_combos_with_a = len([combo for combo in itertools.combinations(elements,k) if 'a' in combo])
print(num_combos_with_a / len(list(itertools.combinations(elements,k))))
