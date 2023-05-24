import sys
import os


_, task_n, n = sys.argv

if os.path.exists(f'tasks/task{task_n}/homework/template.py'):
    with open(f'tasks/task{task_n}/homework/template.py', encoding='utf8') as f:
        data = f.read()
else:
    data = ''

for i in range(int(n)):
    if not os.path.exists(f'tasks/task{task_n}/homework/n{i + 1}.py'):
        with open(f'tasks/task{task_n}/homework/n{i + 1}.py', mode='w', encoding='utf8') as f:
            f.write(data)
