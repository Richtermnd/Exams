import os
import sys


os.chdir('d:/ЕГЭ/tasks/task26/homework/n25/')


def main():
    f = open('26.txt')
    n = int(f.readline())
    a = [int(x) for x in f]
    a.sort()

    weights = [0] * (sum(a) + 1)

    s = 0
    for x in a:
        _weights = weights[:]
        for i in range(s + 1):
            if weights[i]:
                _weights[i + x] = 1
        
        _weights[x] = 1
        weights = _weights
        s += x
    mx = 0
    cnt = 0
    for i in range(1, sum(a) + 1):
        if not weights[i]:
            mx = i
            cnt += 1
    print(cnt, mx)
    

main()
