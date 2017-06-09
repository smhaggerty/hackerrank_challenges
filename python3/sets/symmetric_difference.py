_, m = input(), set(map(int, input().split()))
_, n = input(), set(map(int, input().split()))

sym_diff_m_n = m.symmetric_difference(n)

print(*sorted(sym_diff_m_n), sep='\n')
