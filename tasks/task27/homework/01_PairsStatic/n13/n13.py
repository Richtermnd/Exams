import os


os.chdir('tasks/task27/homework/n13/')


def min_sum(a, b, c):
    pass


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    a = [[] for _ in range(11)]

    for _ in range(n):
        x = int(f.readline())
        a[x % 11].append(x)
    
    for elem in a:
        elem.sort()  # Сортирую, чтобы самые маленькие числа были в начале.

    res = a[0][0] + a[0][1] + a[0][2]  # 0 0 0

    # Каждая переменная цикла - остаток от деления на 11.
    # Переменные вида <переменная цикла>_index - индекс элемента в списке с числами 
    # с соответсвуюшим остатками от деления на 11.
    # Они используются, чтобы избежать повторений чисел.

    for i in range(1, 11 // 2):
        i_index = 0
        for j in range(i, 11 - i):
            # l + i + j == 11 всегда.
            l = 11 - j - i
            j_index = i_index + 1 if j == i else 0

            # Трёх одинаковых быть не может, так что доп проверка не нужна.
            if l == i:
                l_index = i_index + 1
            elif l == j:
                l_index = j_index + 1
            else:
                l_index = 0

            # Дебажить принтами - обожаю.
            print(i, j, l, i + j + l)
            print(i_index, j_index, l_index)
            print(a[i][i_index] + a[j][j_index] + a[l][l_index])
            print()

            res = min(res, a[i][i_index] + a[j][j_index] + a[l][l_index])
    print(res)
            

solution('A')
# solution('B')