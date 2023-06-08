import os


os.chdir('tasks/task27/homework/n33/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n, k = [int(x) for x in f.readline().split()]

    s = 0  # текущая сумма
    l = 0  # длина текущий последовательности
    res = 0  # итоговая длина
    queue = []
    for _ in range(n):
        x = int(f.readline())
        s += x
        l += 1
        queue.append(x)  # Добавляю в очередь в начале, чтобы избежать ситуации, когда первое число уже больше чем контрольное.
        if s > k:
            s -= queue.pop(0)
            l -= 1

        res = max(res, l)

    print(res)


solution('A')
solution('B')
