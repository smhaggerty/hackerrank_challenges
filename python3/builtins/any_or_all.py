# extra-challenge: fit solution on 3 lines
_, data = int(input()), input().split()
isPositive = all(map(lambda x: int(x) > 0, data))
print(isPositive and any([True for elem in data if elem == elem[::-1]]))
