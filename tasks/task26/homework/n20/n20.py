import os
from itertools import combinations


os.chdir('d:/ЕГЭ/tasks/task26/homework/n20/')


def main():
    f = open('26.txt')
    n = int(f.readline())
    a = [int(f.readline()) for _ in range(n)]
    a.sort()
    nums = set(a)

    cnt = 0
    max_sum = 0
    for x, y in combinations(a, r=2):
        if x % 2 == y % 2:
            continue
        
        if x + y not in nums:
            continue
        
        cnt += 1
        max_sum = max(max_sum, x + y)

    print(cnt, max_sum)


main()
