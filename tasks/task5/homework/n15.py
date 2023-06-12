from itertools import permutations


def f(n):
    nums = []
    for x in permutations(str(n), r=2):
        if x[0] == '0':
            continue
        nums.append(int(''.join(x)))

    r1, r2 = max(nums), min(nums)
    return r1 - r2


def solution():
    for i in range(100, 1000):
        if f(i) == 5:
            print(i)
            break

    
solution()