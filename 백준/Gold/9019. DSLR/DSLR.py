from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    q = deque()
    q.append((A, ""))
    visit = [0] * 10000

    while q:
        num, path = q.popleft()
        visit[num] = 1

        if num == B:
            print(path)
            break

        n = (2*num) % 10000
        if not visit[n]:
            q.append((n, path + 'D'))
            visit[n] = 1

        n = (num-1) % 10000
        if not visit[n]:
            q.append((n, path + 'S'))
            visit[n] = 1

        n = (10 * num + (num // 1000)) % 10000
        if not visit[n]:
            q.append((n, path + 'L'))
            visit[n] = 1

        n = (num // 10 + (num % 10) * 1000) % 10000
        if not visit[n]:
            q.append((n, path + 'R'))
            visit[n] = 1