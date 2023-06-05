import os


os.chdir('tasks/task27/homework/n13/')



def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    queue = [int(f.readline()) for _ in range(5)]
    c = [[0] * 13, [0] * 13]
    res = 0
    for _ in range(n - 5):
        x = int(f.readline())
        dif_mod = x % 13
        if x % 2 == 0:
            res += c[0][dif_mod]
            res += c[1][dif_mod]
        else:
            res += c[0][dif_mod]

        c[queue[0] % 2][queue[0] % 13] += 1
        queue.append(x)
        queue.pop(0)
        
    print(res)


solution('A')
solution('B')