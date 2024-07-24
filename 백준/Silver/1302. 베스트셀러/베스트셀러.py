
from collections import defaultdict
n = int(input())
dic = defaultdict()
for _ in range(n):
    book = input()
    if dic.get(book) is None:
        dic[book] = 1
    else:
        dic[book] += 1
mx = max(dic.values())
ans = []
for k, v in dic.items():
    if v == mx:
        ans.append(k)
ans.sort()
print(ans[0])