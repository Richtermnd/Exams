import os
from itertools import combinations


os.chdir('d:/ЕГЭ/tasks/task26/homework/n19/')


def main():
    f = open('26.txt')
    n = int(f.readline())
    a = [int(f.readline()) for _ in range(n)]
    a.sort()
    biggest_lower = a[len(a) // 2 - 1]  # a[2499]
    lowest_bigger=  a[len(a) // 4 * 3]  # a[3750]
    cnt = 0
    min_avg = float('inf')
    for x, y in combinations(a, r=2):
        if (x + y) % 2:
            continue

        avg = (x + y) // 2
        if biggest_lower < avg < lowest_bigger:
            cnt += 1
            min_avg = min(min_avg, avg)
            
    print(cnt, min_avg)


main()
