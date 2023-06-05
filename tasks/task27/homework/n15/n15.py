import os

os.chdir('tasks/task27/homework/n15/')


def solution(var):
    f = open(f'27{var}.txt', mode='r')
    n = int(f.readline())
    queue = [int(f.readline()) for _ in range(4)]
    c_min = [float('inf')] * 137
    c_max = [-float('inf')] * 137
    res = -float('inf')
    for _ in range(n - 4):
        x = int(f.readline())
        diff_mod = x % 137
        
        if c_max[diff_mod] != -float('inf'):
            res = max(res, abs(c_max[diff_mod] - x))
            
        if c_min[diff_mod] != float('inf'):
            res = max(res, abs(c_min[diff_mod] - x))

        c_max[queue[0] % 137] = max(c_max[queue[0] % 137], queue[0])
        c_min[queue[0] % 137] = min(c_min[queue[0] % 137], queue[0])
        queue.append(x)
        queue.pop(0)
    
    print(res)


solution('A')
solution('B')