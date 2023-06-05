import os


os.chdir('tasks/task27/homework/n11/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    queue = [int(f.readline()) for _ in range(5)]
    c = {
        1: 0, 
        3: 0, 
        7: 0, 
        9: 0
    }
    res = 0
    for _ in range(n - 5):
        x = int(f.readline())
        mod = x % 10
        if mod == 1:
            res += c[3]
        elif mod == 3:
            res += c[1]
        elif mod == 7:
            res += c[9]
        elif mod == 9:
            res += c[7]

        if queue[0] % 10 in c:
            c[queue[0] % 10] += 1

        queue.append(x)
        queue.pop(0)
    print(res)


solution('A')
solution('B')