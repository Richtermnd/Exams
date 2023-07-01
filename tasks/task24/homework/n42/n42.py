import os


os.chdir('tasks/task24/homework/n42')


s = open('24.txt').readline().strip()
res = {}
for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
        if s[i + 1] not in res:
            res[s[i + 1]] = 0
        res[s[i + 1]] += 1

c = max(res, key=res.__getitem__)
print(c, res[c], sep='')
