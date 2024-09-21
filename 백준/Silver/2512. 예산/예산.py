
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
result = 0  # 출력해야 하는 최대 예산
start, end = 1, max(lst)  # 1을 시작, 최댓값을 끝
while start <= end:
    mid = (start + end) // 2  # 중앙 원소 고르기
    total = 0  # 예산의 합
    for l in lst:
        if l > mid:
            total += mid
        else:
            total += l
    if total <= m:  # M 이하 이면 중앙값+1 ~ 끝 값 다시 찾기
        result = mid
        start = mid + 1
    else:  # M초과 이면 시작 ~ 중앙값-1 값 다시 찾기
        end = mid - 1
print(result)