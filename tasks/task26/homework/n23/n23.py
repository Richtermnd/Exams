import os
from collections import namedtuple


os.chdir('d:/ЕГЭ/tasks/task26/homework/n23/')


def main():
    f = open('26.txt')
    l, m, n = [int(x) for x in f.readline().split()]

    timeline = [0] * (l + 1)
    for _ in range(n):
        start, dur = [int(x) for x in f.readline().split()]
        finish = start + dur
    
        timeline[start] -= 1
        timeline[finish] += 1
    
    cnt = 0
    max_delay = 0

    k = 0
    st, fn = -1, 0
    for i in range(l + 1):
        k0 = k
        k += timeline[i]

        if k == 0 and st == -1:
            st = i
        # i == l - ключевая хрень, без неё время от завершения последней задачи до конца дня не считывается.
        if k != 0 and k0 == 0 or i == l:
            fn = i
            if fn - st >= m:
                cnt += 1
                max_delay = max(max_delay, fn - st)
            st, fn = -1, 0
    print(cnt, max_delay)

    

main()
