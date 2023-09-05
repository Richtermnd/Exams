def f(n):
    r = str(n)
    nums = [int(r[i: i + 2]) for i in range(len(r) - 1)]
    return max(nums) - min(nums)


def solution():
    for i in range(10, 1000):
        if f(i) == 44:
            print(i)
            break

    
solution()