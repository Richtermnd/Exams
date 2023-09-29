from itertools import permutations

def f(n):
    # convert to nums
    d = [int(x) for x in str(n)]
    nums = list(permutations(d, r=2))
    nums = [x[0] * 10 + x[1] for x in nums]
    nums = [x for x in nums if x >= 10]
    return max(nums) - min(nums)



