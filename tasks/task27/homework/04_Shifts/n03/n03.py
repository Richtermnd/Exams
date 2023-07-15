import os


os.chdir('tasks/task27/homework/04_Shifts/n03')


def solution(var):
    f = open(f'27{var}.txt')
    n, k = [int(x) for x in f.readline().split()]
    a = [int(x) for x in f]
    res = s = a[0]
    st, fn = 0, 1
    while fn + 1 != n:
        fn += 1
        while s + a[fn] > k:
            s -= a[st]
            st += 1
        s += a[fn]
        res = max(res, fn - st)
    print(res)


solution('A')
solution('B')
