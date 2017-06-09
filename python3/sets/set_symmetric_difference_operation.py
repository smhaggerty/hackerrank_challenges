_, english_subs = input(), set(input().split())
_, french_subs = input(), set(input().split())

english_xor_french_subs = len(english_subs.symmetric_difference(french_subs))

print(english_xor_french_subs)
