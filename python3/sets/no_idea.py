_ = input()
elements = map(int, input().split())
like_set = set(map(int, input().split()))
dislike_set = set(map(int, input().split()))
happiness = 0

for element in elements:
    if element in like_set:
        happiness += 1
    elif element in dislike_set:
        happiness -= 1

print(happiness)
