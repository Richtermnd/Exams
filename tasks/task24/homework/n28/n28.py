import os


os.chdir('tasks/task24/homework/n28')


s = open('24.txt').readline().strip()
print(s.count('OCK') - s.count('STOCK'))
