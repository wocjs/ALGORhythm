n = int(input())
arr = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    arr.append([age, name])
arr = sorted(arr, key=lambda x:x[0])
for i in arr:
    print(*i)