import os


os.chdir('tasks/task24/homework/n44')


# Находим строку с наибольшим кол-вом Q
full = ''
last = ''
max_q = 0
for s in open('24.txt'):
    s = s.strip()
    if s.count('Q') >= max_q:
        last = s
        max_q = s.count('Q')
    full += s.strip()

# Самый редкий символ
little_char = min(last, key=lambda x: (last.count(x), x))
print(little_char, full.count(little_char))

