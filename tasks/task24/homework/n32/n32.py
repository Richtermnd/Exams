import os
import re

os.chdir('tasks/task24/homework/n32')


s = open('24.txt').readline().strip()
res = 0
for i in range(len(s) - 3):
    if s[i] + s[i + 2:i + 4] == 'GME':
        res += 1
print(res)

print(len(re.findall('G.ME', s)))  # Не работает при перекрытии.