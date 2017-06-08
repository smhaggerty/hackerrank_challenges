n, m = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]
sort_index = int(input())

for entry in sorted(data, key=lambda x: x[sort_index]):
    print(*entry)
