from collections import Counter
n = int(input())
words = [input().strip() for i in range(n)]
count = Counter(words)
print(len(count))

seen = set()
for word in words:
    if word not in seen:
        print(count[word], end=' ')
        seen.add(word)
