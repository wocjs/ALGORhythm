
import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    order = int(input())
    if not order:
        print(heapq.heappop(heap)) if heap else print(0)
    else:
        heapq.heappush(heap, order)