import os


os.chdir('tasks/task24/homework/n37')


res = 0
for s in open('24.txt'):
    temp = s
    while 'AOAOA' in temp:
        temp = temp.replace('AOAOA', 'AOA AOA')
    aoa = temp.count('AOA')
    
    temp = s
    while 'OAOAO' in temp:
        temp = temp.replace('OAOAO', 'OAO OAO')
    oao = temp.count('OAO')
    res += aoa > oao

print(res)
