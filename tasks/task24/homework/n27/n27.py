import os


os.chdir('tasks/task24/homework/n27')


s = open('24.txt').readline().strip()
print(s.count('TIK') + s.count('TOK'))
