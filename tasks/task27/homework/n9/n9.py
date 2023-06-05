import os


os.chdir('tasks/task27/homework/n9/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    queue = [int(f.readline()) for _ in range(8)]
    c = 0
    c23 = 0
    res = 0
    for _ in range(n - 8):
        x = int(f.readline())
        if x % 23 == 0:
            res += c
        else:
            res += c23
        
        c += 1
        c23 += queue[0] % 23 == 0
        queue.append(x)
        queue.pop(0)
    
    print(res)


solution('A')
solution('B')