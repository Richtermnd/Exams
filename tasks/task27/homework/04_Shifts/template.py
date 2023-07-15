import os


os.chdir('tasks/task27/homework/04_Shifts/n_')


def solution(var):
    f = open(f'27{var}.txt')
    n, m = [int(x) for x in f.readline().split()]
    a = [int(x) for x in f]
    res = 0
    st, fn = 0, 0
    for i in range(n):
        pass

    print(res)


solution('A')
solution('B')
