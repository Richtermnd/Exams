import os


os.chdir('tasks/task27/homework/05_PartialSums/n09')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    subsequences = []
    res = []
    for _ in range(n):
        x = int(f.readline())
        # Длину делаем отрицательной, чтобы max выбрал последовательность наименьшей длины.
        subsequences = [(a[0] + x, a[1] - 1) for a in subsequences] + [(x, -1)]
        subsequences = {s[0] % 69: s for s in sorted(subsequences)}
        if 0 in subsequences:
            res.append(subsequences[0])
        subsequences = list(subsequences.values())
    print(abs(max(res)[1]))  # Беру модуль, чтобы легче копировать.


solution('A')
solution('B')
