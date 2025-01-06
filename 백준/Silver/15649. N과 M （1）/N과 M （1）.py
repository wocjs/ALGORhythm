from itertools import permutations

n, m = map(int, input().split())
nms = [i for i in range(1, n+1)]

arr = permutations(nms, m)

for i in arr:
    for j in i:
        print(j, end = ' ')
    print()