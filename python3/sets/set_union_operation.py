_, english_subs = input(), set(input().split())
_, french_subs = input(), set(input().split())

english_or_french_subs = len(english_subs.union(french_subs))

print(english_or_french_subs)
