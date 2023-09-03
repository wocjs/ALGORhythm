
def calc_incl(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)


n = int(input())
arr = list(map(int, input().split()))

cnt_lst = [0] * n
for idx, height in enumerate(arr):
    incl_lst = [0] * n
    for i in range(idx+1, n):
        incl_lst[i] = calc_incl(idx, height, i, arr[i])
    for i in range(idx-1, -1, -1):
        incl_lst[i] = -calc_incl(idx, height, i, arr[i])
    cnt = 0
    # print(incl_lst)   # [-1.25, -0.33, -1.5, -4.0, 0, -3.0, -2.0, 0.0, -0.5, -0.8, -0.17, 0.14, -0.38, -0.56, -0.1]
    tmp = -float('inf')
    for i in range(idx + 1, n):
        if incl_lst[i] > tmp:
            tmp = incl_lst[i]
            cnt += 1
            # print(tmp)
    tmp = -float('inf')
    for i in range(idx - 1, -1, -1):
        if incl_lst[i] > tmp:
            tmp = incl_lst[i]
            cnt += 1
            # print(tmp)
    # print()
    cnt_lst[idx] = cnt
print(max(cnt_lst))