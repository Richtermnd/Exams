alph = 'AB'
vowels = 3
concanate = 5


def solution():
    def calc(word):
        res = 1
        for c in word:
            if c == 'A':
                res *= vowels
            else:
                res *= concanate
        return res

    def comb(word: str):
        vowels_count = word.count('A')
        concanate_count = word.count('B')
        if vowels_count > 5 or concanate_count > 5:
            return 0
        if len(word) == 10:
            if vowels_count != concanate_count:  # перестраховка
                return 1
            return calc(word)
        return sum(comb(word + c) for c in alph)
    
    return sum(comb(c) for c in alph)


print(solution())