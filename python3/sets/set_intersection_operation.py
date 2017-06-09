_, english_subs = input(), set(input().split())
_, french_subs = input(), set(input().split())

english_and_french_subs = len(english_subs.intersection(french_subs))

print(english_and_french_subs)
