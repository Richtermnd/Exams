"""	
№ 7664 (Уровень: Сложный)
(Грачев Н.) Логическая функция F задаётся выражением  ((a and b) == (not c)) and (b ? d)
c	a	d	b	F
1	0	0	0	1
1	0	1	0	1
1	0	1	1	1
1	1	0	0	1
Определить пропущенную логическую операцию
1) И
2) Эквиваленция
3) Импликация
4) Или
"""

import operator

def check(a, b, c, d, f, func):
    return ((a and b) == (not c)) and func(b, d) == f


op_list = [operator.and_, operator.eq, operator.le, operator.or_]

args = [
    # a b c d f
    (0, 0, 1, 0, 1),
    (0, 0, 1, 1, 1),
    (0, 1, 1, 1, 1),
    (1, 0, 1, 0, 1)
]

for op in op_list:
    func = lambda args: check(*args, op)
    if all(map(func, args)):
        print(op.__name__)


# ответ: 3