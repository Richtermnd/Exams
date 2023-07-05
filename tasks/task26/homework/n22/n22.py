import os


os.chdir('d:/ЕГЭ/tasks/task26/homework/n22/')


def main():
    f = open('26.txt')
    n = int(f.readline())
    a = [[int(x) for x in f.readline().split()] for _ in range(n)]
    
    road = [0] * 2_000_000
    for st, fn in a:
        road[st] += 1
        road[fn] -= 1

    k = 0
    st, fn = -1, 0
    cnt = 0
    length = 0
    for i in range(2_000_000):
        k0 = k
        k += road[i]
        if k > 0 and st == -1:
            st = i
        if k == 0 and k0 > 0:
            fn = i
            cnt += 1
            length += fn - st
            st, fn = -1, 0
    
    print(cnt, length)


main()
