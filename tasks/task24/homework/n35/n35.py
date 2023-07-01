import os


os.chdir('tasks/task24/homework/n35')


res = 0
for s in open('24.txt'):
    res += s.count('B') / s.count('A') >= 1.05

print(res)
