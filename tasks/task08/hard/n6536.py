import itertools as it


res = set(it.permutations('AAAAABBB'))
starts_with_b = sum(1 for elem in res if elem[0] == 'B')
starts_with_a = sum(1 for elem in res if elem[0] == 'A')

cnt = starts_with_a * 8 ** 8 + starts_with_b * 7 * 8 ** 7
print(cnt)
