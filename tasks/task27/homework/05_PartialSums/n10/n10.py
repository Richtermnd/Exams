import os


os.chdir('tasks/task27/homework/05_PartialSums/n10')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    subsequences = []
    res = []
    for _ in range(n):
        x = int(f.readline())
        # Длину делаем отрицательной, чтобы min брал наиболее длинную последовательность.
        subsequences = [(a[0] + x, a[1] - 1) for a in subsequences] + [(x, -1)]
        subsequences = {s[0] % 2077: s for s in sorted(subsequences, reverse=True)}
        if 0 in subsequences:
            res.append(subsequences[0])
        subsequences = list(subsequences.values())
    print(abs(min(res)[1]))


solution('A')
solution('B')
