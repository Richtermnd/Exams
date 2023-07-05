import os


os.chdir('d:/ЕГЭ/tasks/task26/homework/n18/')


def main():
    f = open('26.txt')
    n, s = [int(x) for x in f.readline().split()]
    a = [int(f.readline()) for _ in range(n)]
    a.sort(reverse=True)

    cnt = 0
    while a:
        s1 = 0
        for i in range(len(a)):
            if s1 + a[i] <= s:
                s1 += a[i]
                a[i] = 0
        a = [x for x in a if x]
        cnt += 1
    
    print(cnt, s1)


main()
