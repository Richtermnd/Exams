import os
import string


os.chdir('tasks/task24/homework/n6')


s = open('24.txt').readline()
for c in string.ascii_lowercase:
    s = s.replace(c, ' ')

s = s.split()
print(max(len(x) for x in s))
