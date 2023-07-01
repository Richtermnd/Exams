import os
import re


os.chdir('tasks/task24/homework/n36')

res = 0
for s in open('24.txt'):
    res += bool(re.match('\w*K.GE\w*', s))

print(res)
