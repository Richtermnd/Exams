import os


os.chdir('tasks/task27/homework/n12/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    data = [int(f.readline()) for _ in range(n)]

    res = 0
    for i in range(n - 1):
        for j in range(i + 1, min(i + 8, n)):
            # print(i, j)
            assert j - i <= 7, f'{j} {i}'
            if (data[i] + data[j]) % 8 != 0:
                res += 1
    
    print(res)


solution('A')
solution('B')