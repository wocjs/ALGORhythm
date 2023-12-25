import heapq
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    n = int(input())
    visited = [0] * n
    minH, maxH = [], []
    for i in range(n):
        order, num = input().split()
        num = int(num)

        if order == 'I':
            heapq.heappush(minH, (num, i))
            heapq.heappush(maxH, (-num, i))
            visited[i] = 1   # minH, maxH 어떤 힙에서도 삭제되지 않은 상태

        # 최소힙과 최대힙을 동기화 시켜줘야 함
        elif num == 1:   # maxH에서 삭제
            # 이미 삭제된 노드면 삭제되지 않은 노드 나올때까지 다 버림
            while maxH and not visited[maxH[0][1]]: # visited가 0 -> 해당노드가 삭제된 상태
                heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]] = 0
                heapq.heappop(maxH)
        elif num == -1:  # minH에서 삭제
            while minH and not visited[minH[0][1]]:
                heapq.heappop(minH)
            if minH:
                visited[minH[0][1]] = 0
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    if maxH and minH:
        print(-maxH[0][0], minH[0][0])
    else:
        print("EMPTY")