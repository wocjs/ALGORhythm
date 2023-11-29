k = int(input())
arr = []
for _ in range(k):
    n = int(input())
    if n:
        arr.append(n)
    else:
        arr.pop()
print(sum(arr))