import os


os.chdir('tasks/task24/homework/n10')


s = open('24.txt').readline()
while 'XX' in s or 'YY' in s or 'ZZ' in s:
    s = s.replace('XX', 'X X').replace('YY', 'Y Y').replace('ZZ', 'Z Z')
s = s.split()
print(max(len(x) for x in s))
