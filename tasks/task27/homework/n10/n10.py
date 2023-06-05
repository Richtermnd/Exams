import os


os.chdir('tasks/task27/homework/n10/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    queue = [int(f.readline()) for _ in range(4)]
    c = [0, 0]  # чет, нечет
    c13 = [0, 0]  # чет, нечет

    res = 0
    for _ in range(n - 4):
        x = int(f.readline())
        if x % 13 == 0:
            res += c[not (x % 2)]
        else:
            res += c13[not (x % 2)]

        c[queue[0] % 2] += 1
        c13[queue[0] % 2] += queue[0] % 13 == 0

        queue.append(x)
        queue.pop(0)

    
    print(res)


solution('A')
solution('B')