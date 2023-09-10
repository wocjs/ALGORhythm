import heapq
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()  # 시작시간 기준 ort

# 우선순위 큐 <- 제일 빠른 종료시간 기준 정렬
pq = []

# 1번째 종료시간 heappush
heapq.heappush(pq, arr[0][1])

# 2
for i in range(1, n):
    # i번째 시작시간과 제일 빠른 종료시간 비교
    if arr[i][0] >= pq[0]:
        heapq.heappop(pq)
    heapq.heappush(pq, arr[i][1])

print(len(pq))