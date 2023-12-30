T = int(input())
for tc in range(T):
    clothes = {}
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        if clothes.get(b) == None:
            clothes[b] = set()
        clothes[b].add(a)

    cnt = 1
    for k in clothes.keys():
        cnt *= len(clothes[k]) + 1
    print(cnt - 1)