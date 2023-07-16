import os


os.chdir('tasks/task27/homework/05_PartialSums/n07')


def solution(var):
    f = open(f'27{var}.txt')
    n = int(f.readline())
    subsequences = []
    res = []
    for _ in range(n):
        x = int(f.readline())
        subsequences = [a + x for a in subsequences] + [x]
        subsequences = {x % 1000: x for x in sorted(subsequences)}
        if 0 in subsequences:
            res.append(subsequences[0])
        subsequences = list(subsequences.values())
    print(max(res))


solution('A')
solution('B')
