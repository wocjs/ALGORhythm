
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def find(arr1, arr2, res = []):
    if (not arr1) or (not arr2):
        return res

    mx1, mx2 = max(arr1), max(arr2)
    i1, i2 = arr1.index(mx1), arr2.index(mx2)

    # 두 값이 같으면 결과 추가하고 그 뒷부분 재귀
    if mx1 == mx2:
        res.append(mx1)
        return find(arr1[i1+1:], arr2[i2+1:], res)
    # tmp1이 더 크면 arr1에서 제거, 재귀
    elif mx1 > mx2:
        arr1.pop(i1)
        return find(arr1, arr2, res)
    else:
        arr2.pop(i2)
        return find(arr1, arr2, res)


n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

ans = find(arr1, arr2)
print(len(ans))
if ans:
    print(*ans)