import os


os.chdir('tasks/task24/homework/n38')


s = open('24.txt').readline().strip()
res = 0

for i in range(len(s) - 6):
    if s[i] == 'A':
        for j in range(i + 6, min(len(s), i + 10)):
            if s[j] == 'F':
                res += 1

print(res)
