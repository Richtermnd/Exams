import os


os.chdir('tasks/task27/homework/01_PairsStatic/n15/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [[] for _ in range(80)]
    for _ in range(n):
        x = int(f.readline())
        a[x % 80].append(x)
    
    res = 0
    for elem in a:
        elem.sort()
        if len(elem) >= 2:
            res = max(res, elem[-1] - elem[0])
    print(res)


solution('A')
solution('B')