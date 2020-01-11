from itertools import permutations

print('\n'.join(map(lambda x: ''.join(map(str, x)), permutations(range(1, int(input()) + 1)))))
