import os
from collections import Counter


os.chdir('tasks/task24/homework/n40')


s = open('24.txt').readline().strip()
print(Counter(s).most_common())

