def solve():
  chk = [0]*(W+1)
  for i in range(N):
    for j in range(i+1,N):
      w = wei[i] + wei[j]
      if w<=W:
        chk[w] = (i,j)
  for i in range(N):
    for j in range(i+1,N):
      w = wei[i] + wei[j]
      if w<=W and chk[W-w]:
        if i not in chk[W-w] and j not in chk[W-w]:
          return 1

W,N = map(int,input().split())
wei = list(map(int, input().split()))
print("YES" if solve() else "NO")