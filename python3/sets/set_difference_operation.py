_, english_subs = input(), set(input().split())
_, french_subs = input(), set(input().split())

english_only_subs = len(english_subs.difference(french_subs))

print(english_only_subs)
