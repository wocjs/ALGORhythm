for tc in range(1, int(input())+1):
    arr = list(map(str, input().split()))
    print(f"Case #{tc}: {' '.join(arr[::-1])}")