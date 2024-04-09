import sys
sys.stdin = open('../input.txt', 'r')
#####
# https://www.codetree.ai/training-field/frequent-problems/problems/unstable-moving-walk/description?page=2&pageSize=20
# 1540 start 1632 end
from collections import deque
def cntz():
    cnt = 0
    for i in range(n*2):
        if arr[i] == 0:
            cnt += 1
    if cnt >= k:
        return False
    return True


n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
arr = deque(arr)
people = [0]*2*n
people = deque(people)
while cntz():
    ans += 1
    # 무빙워크 회전
    arr.appendleft(arr.pop())
    people.appendleft(people.pop())
    if people[n-1]:
        people[n-1] = 0

    # 2. 앞쪽부터 한칸씩 이동 가능한지
    for i in range(n-2, -1, -1):
        if arr[i+1] and people[i] and people[i+1] == 0:
            people[i] = 0
            people[i+1] = 1
            arr[i+1] -= 1
    if people[n-1]:
        people[n-1] = 0

    # 3. 사람 올리기
    if arr[0] > 0 and people[0] == 0:
        people[0] = 1
        arr[0] -= 1
    if people[n-1]:
        people[n-1] = 0
    # print(arr)
    # print(people)
    # print()
print(ans)