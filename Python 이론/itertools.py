from itertools import permutations
from itertools import combinations

print('permutations')
for per in permutations([1,3,5,7],2):
  print(per)

print('combinations')
for comb in combinations([1,2,3,4],2):
  print(comb)