import os


os.chdir('d:/ЕГЭ/tasks/task26/homework/n16/')


def main():
    f = open('26.txt')
    s, n = [int(x) for x in f.readline().split()]
    a = []
    for _ in range(n):
        a.append(int(f.readline()))
    a.sort()

    res = []
    while sum(res) + a[-1] <= s:
        res.append(a.pop())
        a = a[::-1]
    
    print(len(res), res[-1])


main()
