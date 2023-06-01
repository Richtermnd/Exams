"""
Не решено
"""

import math

ans = 2662222227200

# для n гласных - C(n, k) * 21 ** (10 - n) * 5 ** n
res = 0
for i in range(2, 6):
    # варианты перестановок гласных
    temp = math.comb(10, i)
    print(temp)
    breakpoint()
    
    # согласные
    consonant = math.perm(21, 10 - i)
    print(consonant)
    breakpoint()
    temp *= consonant
    
    # гласные
    vowels = math.perm(5, i)
    print(vowels)
    breakpoint()
    temp *= vowels

    res += temp
    print(res)
    # print(ans / res)


print()
print(res)
print(ans)
print(res / ans)
# assert res == 2662222227200, res