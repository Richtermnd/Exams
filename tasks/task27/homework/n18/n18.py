import os


os.chdir('tasks/task27/homework/n18/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    # c = [[] for _ in range(134)]  # массив счётчиков 
    c = [0] * 134
    res = 0
    for _ in range(n):
        x = int(f.readline())
        if x > 134:
            continue

        for i in range(x + 1, 134):
            if x + i <= 134:
                res += c[i]
        
        c[x] += 1

    print(c[67:])
    print(res)


solution('A')
solution('B')