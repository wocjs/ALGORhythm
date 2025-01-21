from collections import deque

n, d = map(int, input().split())
dp = [0]
dp.extend(map(int, input().split()))
deq = deque()
for i in range(1, n+1):
    while deq:
        if deq[0][0] < i-d:
            deq.popleft() 
        else:
            dp[i] = max(dp[i], dp[i]+deq[0][1])
            break
    while deq:
        if deq[-1][1] < dp[i]:
            deq.pop()
        else:
            break
    deq.append((i, dp[i]))
print(max(dp[1:]))