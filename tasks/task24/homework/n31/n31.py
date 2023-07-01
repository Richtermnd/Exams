import os
import re


os.chdir('tasks/task24/homework/n31')


s = open('24.txt').readline().strip()
while 'XXXXX' in s:
    s = s.replace('XXXXX', 'XXXX XXXX')
print(s.count('XXXX'))
