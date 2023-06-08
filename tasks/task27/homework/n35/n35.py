import os


os.chdir('tasks/task27/homework/n35/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n, k, m = [int(x) for x in f.readline().split()]

    a = []
    for _ in range(n):
        dist, c = [int(x) for x in f.readline().split()]
        dist = dist % k
        c = c // 9 + (c % 9 != 0)
        a.append([dist, c])
        a.append([k + dist, c])
    
    a.sort()

    def dist(x, y):
        return a[x][0] - a[y][0]
    
    start, finish = 0, 0
    s = a[0][1]
    while dist(finish + 1, start) <= m:
        finish += 1
        s += a[finish][1]
    res = s

    for cur in range(finish, n + finish):
        while finish + 1 < n + finish and dist(finish + 1, cur) <= m:
            finish += 1
            s += a[finish][1]
        
        while dist(cur, start) > m:
            s -= a[start][1]
            start += 1
        
        res = max(res, s)

    print(res)


solution('A')
solution('B')
