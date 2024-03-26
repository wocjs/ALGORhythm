n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []
res = arr1 + arr2
print(*sorted(res))