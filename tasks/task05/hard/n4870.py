from itertools import permutations


def f(n):
    nums = []
    for x in permutations(str(n), r=2):
        if x[0] == '0':
            continue
        nums.append(int(''.join(x)))
    return max(nums) - min(nums)


def solution():
    cnt = 0
    for i in range(300, 401):
        if f(i) == 20:
            cnt += 1
    print(cnt)


solution()