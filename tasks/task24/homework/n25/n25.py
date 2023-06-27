import os

os.chdir('tasks/task24/homework/n25')


s = open('24.txt').readline()

res = 0
for i in range(300):
    sub = 'DBAC' * i
    if sub in s:
        for ext in 'DBA':
            if sub + ext not in s:
                break
            sub += ext

        res = max(res, len(sub))

print(res)