from itertools import permutations


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def f(n):
    nums = []
    for x in permutations(str(n), r=2):
        if x[0] == '0':
            continue
        nums.append(int(''.join(x)))
    nums = [x for x in nums if is_prime(x)]
    return len(set(nums))
    

def solution():
    res = 100
    for i in range(100, 1000):
        res = max(res, i, key=lambda x: (f(x), x))

    print(res)
    

solution()