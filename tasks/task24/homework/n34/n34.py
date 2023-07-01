import os


os.chdir('tasks/task24/homework/n34')


res = 0
for s in open('24.txt'):
    res += s.count('X') == s.count('S')

print(res)
