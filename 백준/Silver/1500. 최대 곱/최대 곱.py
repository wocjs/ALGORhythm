
s, k = map(int, input().split())
li = [s // k for _ in range(k)]
# print(li)
for i in range(s % k):
    li[i] += 1
# print(li)
res = 1
for n in li:
    res *= n
print(res)
