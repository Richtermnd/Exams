import os


os.chdir('tasks/task27/homework/01_PairsStatic/n04/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a5_odd, a5_even = 0, 0
    a_odd, a_even = 0, 0
    for _ in range(n):
        x = int(f.readline())
        if x % 2 == 0 and x % 5 == 0:
            a5_even += 1
        elif x % 2 == 0 and x % 5 != 0:
            a_even += 1
        elif x % 2 != 0 and x % 5 == 0:
            a5_odd += 1
        else:
            a_odd += 1

    res = 0
    res += a5_even * a5_odd
    res += a5_even * a_odd
    res += a5_odd * a_even
    print(res)


solution('A')
solution('B')