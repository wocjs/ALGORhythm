
'''
시간복잡도 제일 적은 풀이법.
현재까지 경로를 메모이제이션하여 다음 루트를 방문했다면 prunning
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y, cnt, _st):
	global ans
	ans = max(ans, cnt)
	if ans == 26:		# 되는지도 모르겠는 prunning
		return
	
	for dx, dy in dr:
		nx, ny = x + dx, y + dy
		if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] not in _st:
			# use memoization
			if memo[nx][ny][0] == _st + arr[nx][ny]:
				ans = max(ans, memo[nx][ny][1])
				continue
			_st += arr[nx][ny]
			dfs(nx, ny, cnt + 1, _st)
			_st = _st[:-1]
	
	memo[x][y] = [_st, cnt]

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
st = str(arr[0][0])
ans = 0
memo = [[['', 0]] * m for _ in range(n)]
dfs(0, 0, 1, st)
print(ans)

'''
##### 기본적인 백트래킹인데 문제 너무 더러움
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# list 안붙였다고 시간초과 뜨는건 좀 아니다;;
# arr = [input() for _ in range(n)]
# arr = [input().strip() for _ in range(n)]
arr = [list(input()) for _ in range(n)]

st = set()
ans = 0
# dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
	global ans
	ans = max(ans, cnt)
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
#		if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] not in st:
		if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny] in st:
			st.add(arr[nx][ny])
			dfs(nx, ny, cnt + 1)
			st.remove(arr[nx][ny])
	
st.add(arr[0][0])
dfs(0, 0, 1)
print(ans)
'''