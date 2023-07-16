import os


os.chdir('tasks/task27/homework/05_PartialSums/n08')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    subsequences = []
    res = []
    for _ in range(n):
        x = int(f.readline())
        subsequences = [(a[0] + x, a[1] + (x % 5 == 0)) for a in subsequences] + [(x, x % 5 == 0)]
        subsequences = {c % 3: (s, c) for s, c in sorted(subsequences)}
        if 0 in subsequences:
            res.append(subsequences[0][0])
        subsequences = list(subsequences.values())
    print(max(res))


solution('A')
solution('B')
