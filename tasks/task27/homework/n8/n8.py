import os


os.chdir('tasks/task27/homework/n8/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    big_nums = [0] * 80
    small_nums = [0] * 80

    for _ in range(n):
        x = int(f.readline())
        if x > 50_000:
            big_nums[x % 80] += 1
        else:
            small_nums[x % 80] += 1


    # +------------------------------------------------------+
    # | У четного числа два частных случая - нули и середина |
    # +------------------------------------------------------+

    res = big_nums[0] * (big_nums[0] - 1) // 2
    res += big_nums[40] * (big_nums[40] - 1) // 2
    res += big_nums[0] * small_nums[0]

    # Пары больших цифр
    for i in range(1, 40):
        res += big_nums[i] * big_nums[80 - i]
    
    for i in range(1, 80):
        res += big_nums[i] * small_nums[80 - i]
    print(res)


solution('A')
solution('B')