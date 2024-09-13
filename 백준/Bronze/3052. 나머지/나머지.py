
arr = []
for _ in range(10):
    s = int(input()) % 42
    if s not in arr:
        arr.append(s)
print(len(arr))