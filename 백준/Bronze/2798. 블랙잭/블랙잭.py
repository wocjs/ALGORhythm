# B2798
from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
sm = 0

for cards in combinations(arr, 3):
    tmpSm = sum(cards)
    if sm < tmpSm <= m:
        sm = tmpSm
print(sm)