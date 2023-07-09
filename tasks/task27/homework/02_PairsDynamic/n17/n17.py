import os


os.chdir('tasks/task27/homework/02_PairsDynamic/n17/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [int(x) for x in f]
    res = float('inf')
    mods = [[[] for _ in range(1071)] for _ in range(2)]
    # Chad solution.
    for i in range(1, n):
        # Т.к. начинаем с 1, то сначала обновляем статистику, а уже потом считаем результат.
        x = a[i - 1]
        mods[x % 2][x % 1071].append(a[i - 1])
        
        if i > 11:
            # Чистим элемент, который отдалился
            x = a[i - 11 - 1]
            # Самый первый элемент - тот кто вошел в последовательность раньше всех.
            mods[x % 2][x % 1071].pop(0)
        
        x = a[i]
        mod = 0 if x % 1071 == 0 else 1071 - x % 1071
        if mods[x % 2][mod]:
            res = min(res, x + min(mods[x % 2][mod]))
    
    """
    # Pussy solution
    for i in range(n - 11):
        for j in range(i + 1, i + 12):
            s = a[i] + a[j] 
            if s % 2 == 0 and s % 1071 == 0:
                res = min(res, s)
    """    
    print(res)


solution('A')
solution('B')