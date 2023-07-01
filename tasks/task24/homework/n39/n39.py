import os


os.chdir('tasks/task24/homework/n39')


s = open('24.txt').readline().strip()
res = 0
for i in range(len(s) - 4):
    if s[i:i + 5] == s[i + 4:i - 1:-1]:
        res += 1

print(res)
