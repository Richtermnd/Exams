import os

os.chdir('tasks/task24/homework/n24')


s = open('24.txt').readline()

res = 0
for i in range(300):
    sub = 'CA' * i
    if sub in s:
        is_uncomplited = sub + 'C' in s
        res = max(res, len(sub) + is_uncomplited)

print(res)