def f(n):
    nums = [int(x) for x in str(n)]
    r1 = str(nums[0] ** 2 + nums[1] ** 2) 
    r2 = str(nums[1] ** 2 + nums[2] ** 2) 
    r = str(max(r1, r2)) + str(min(r1, r2))
    return int(r)


def solution():
    for i in range(100, 1000):
        # print(i, f(i))
        if f(i) == 9010:
            print(i)
            break
        
    
solution()