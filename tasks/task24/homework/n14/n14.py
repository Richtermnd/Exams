import os


os.chdir('tasks/task24/homework/n14')


s = open('24.txt').readline()

s = s.split('D')
print(s[1:10])

print(min(len(x) + 2 if x else float('inf') for x in s[1:-1]))