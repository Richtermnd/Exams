def solution():
    alph = {'г', 'о', 'л'}
    def comb(word):
        if len(word) == 20:
            if word[-1] == 'г':
                return 0
            return 1
        if word[-1] == 'г':
            return comb(word + ('о' if word[-2] == 'л' else 'л'))
        else:
            return sum([comb(word + c) for c in alph - {word[-1]}])
    return comb('о') + comb('л')


print(solution())