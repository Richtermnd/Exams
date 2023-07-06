import os


os.chdir('tasks/task27/homework/n12/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    odd, even = 0, 0
    odd23, even23 = 0, 0
    for _ in range(n):
        x = int(f.readline())
        if x % 23 == 0 and x % 2 == 0:
            even23 = max(even23, x)
        elif x % 23 == 0 and x % 2 != 0:
            odd23 = max(odd23, x)
        elif x % 2 == 0:
            even = max(even, x)
        else:
            odd = max(odd, x)
    res = max(
        odd23 + odd23,
        even23 + even23,
        odd23 + odd,
        even23 + even
    )
    print(res)


solution('A')
solution('B')