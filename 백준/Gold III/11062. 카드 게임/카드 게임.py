import sys


def cal(n, lst):
    turn = True if n % 2 else False
    dp = [[0 for _ in range(n)] for _ in range(n)]

    if turn:
        for i in range(n): 
            dp[i][i] = lst[i]

    for gap in range(1, n):
        turn = not turn
        for i in range(n - gap):
            j = i + gap
            if turn:    dp[i][j] = max(lst[i] + dp[i+1][j], dp[i][j-1] + lst[j])
            else:       dp[i][j] = min(dp[i+1][j], dp[i][j-1])
        
    
    return dp[0][n-1]

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    lst = list(map(int, sys.stdin.readline().split()))
    print(cal(n, lst))