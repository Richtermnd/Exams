import itertools as it


def solution():
    def comb(is_s: bool, cur_len: int):
        if cur_len == 16:
            res = 0 if is_s else 3
            return res
        
        if is_s:
            res = comb(False, cur_len + 1)
            return res
        
        else:
            return 3 * (comb(False, cur_len + 1) + comb(True, cur_len + 1))
        
    return 4 * (comb(False, 2) + comb(True, 2))


def solution_b():
    """
    s - s
    _ - не s
    """
    res = it.product('s_', repeat=14)
    res = map(lambda x: ''.join(x), res)
    res = filter(lambda x: 'ss' not in x, res)
    res = list(res)
    cnt = 0
    values = {
        '_': 3,
        's': 1
    }
    for line in res:
        print('_' + line + '_')
        temp = 1
        for c in line:
            temp *= values[c]
        cnt += temp

    return 4 * cnt * 3

res = solution()
answer = 1590517620
print(f'Res: {str(res).rjust(len(str(answer)))}')
print(f'Ans: {answer}')
print(f'Dif: {answer / res}')

    