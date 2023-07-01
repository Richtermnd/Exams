import os
from collections import Counter


os.chdir('tasks/task24/homework/n43')


s = open('24.txt').readline().strip()
res = Counter()

for i in range(len(s) - 4):
    if s[i:i + 2] + s[i + 3:i + 5] == 'CBBC':
        # print(s[i:i + 5])
        # print(s[i:i + 2] + s[i + 3:i + 5])
        if s[i + 2] not in res:
            res[s[i + 2]] = 0
        res[s[i + 2]] += 1
print(res)
print(res.most_common(1))

