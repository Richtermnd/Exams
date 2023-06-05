import os


os.chdir('tasks/task27/homework/n14/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    data = [int(f.readline()) for _ in range(n)]
    res = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (data[i] + data[j]) % 144 == 0 and data[i] < data[j]:
                res = min(data[i] + data[j], res)
    
    print(res)


solution('A')
solution('B')