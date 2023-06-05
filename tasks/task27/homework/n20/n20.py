import os


os.chdir('tasks/task27/homework/n20/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    data = [int(f.readline()) for _ in range(n)]
    res = float('inf')
    for i in range(n):
        for j in range(i + 5, n, 5):
            assert (j - i) % 5 == 0
            a, b = data[i], data[j]
            if (a + b) % 107 == 0:
                assert (a + b) % 107 == 0  # Топ 1000 по адекватности
                res = min(res, data[i] + data[j])
    assert res % 107 == 0
    print(res)


solution('A')
solution('B')