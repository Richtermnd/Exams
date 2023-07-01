import os
from collections import Counter


os.chdir('tasks/task24/homework/n41')


s = open('24.txt').readline().strip()
res = Counter(s).most_common()
print(res[0][1] - res[-1][1])
