import os


os.chdir('tasks/task27/homework/n17/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    data = [int(f.readline()) for _ in range(n)]
    res = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, min(i + 12, n)):
            assert j - i <= 11
            a, b = data[i], data[j]
            if (a + b) % 2 == 0 and (a + b) % 1071 == 0:
                res = min(res, a + b)
    
    assert res % 2 == 0
    assert res % 1071 == 0
    
    print(res)


solution('A')
solution('B')