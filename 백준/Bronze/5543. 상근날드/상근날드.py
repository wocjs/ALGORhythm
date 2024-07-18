arr = [int(input()) for _ in range(5)]
bg, dr = min(arr[:3]), min(arr[3:])
print(bg + dr - 50)