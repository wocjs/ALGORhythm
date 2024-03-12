from collections import defaultdict


def get_record(n, gifts, index):   # 선물 기록 저장 2차원 배열
    arr = [[0] * n for _ in range(n)]
    for _rec in gifts:
        sender, receiver = _rec.split()
        arr[index[sender]][index[receiver]] += 1
    return arr


def cal_gift_idx(rec, n):  # 선물 지수 행렬
    giftidx = [0] * n
    _rec = list(zip(*rec))  # 전치행렬 - 받은 선물 체크
    for i in range(n):
        giftidx[i] = sum(rec[i]) - sum(_rec[i])
    return giftidx


def solution(friends, gifts):
    index = defaultdict()
    for i, friend in enumerate(friends):
        index[friend] = i
    n = len(index)
    # print(index)    # defaultdict(None, {'muzi': 0, 'ryan': 1, 'frodo': 2, 'neo': 3})
    rec = get_record(n, gifts, index)
    giftidx = cal_gift_idx(rec, n)

    ans = 0
    cnt = [0] * n
    for i in range(n):
        for j in range(i, n):
            if rec[i][j] > 0 or rec[j][i] > 0:  # 둘중 선물 이력이 있으면
                if rec[i][j] > rec[j][i]:
                    cnt[i] += 1
                elif rec[i][j] < rec[j][i]:
                    cnt[j] += 1
                else:   # 같으면 선물지수로 판단
                    if giftidx[i] > giftidx[j]:
                        cnt[i] += 1
                    elif giftidx[i] < giftidx[j]:
                        cnt[j] += 1
            else:   # 둘 다 0이면 == 서로 선물 보낸적 없으면
                if giftidx[i] > giftidx[j]:
                    cnt[i] += 1
                elif giftidx[i] < giftidx[j]:
                    cnt[j] += 1
    ans = max(cnt)

    return ans
