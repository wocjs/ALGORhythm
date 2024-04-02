
import sys
input = sys.stdin.readline
dr = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # 위, 아래, 오, 왼
n, m, k = map(int, input().split())
sharks = {}
for i in range(1, k+1):
    r, c, s, d, z = map(int, input().split())
    sharks[i] = [r-1, c-1, s, d-1, z]
ans = 0
for j in range(m):
    if len(sharks) == 0:
        break
    # 상어 잡음
    for i in range(n):
        for sid in range(1, k+1):
            if sharks.get(sid) is None:
                continue
            r, c, s, d, z = sharks[sid]
            if [i, j] == [r, c]:
                ans += z
                del sharks[sid]
                break
        else:
            continue
        break
    # 최종 위치 저장용
    arr = [[[] for _ in range(m)] for _ in range(n)]
    # 상어 움직임
    for sid in range(1, k+1):
        if sharks.get(sid) is None:
            continue
        r, c, s, d, z = sharks[sid]
        dx, dy = dr[d]
        for i in range(s):
            nx, ny = r + dx, c + dy
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                if d % 2 == 1:
                    d -= 1
                else:
                    d += 1
                dx, dy = dr[d]
                nx, ny = r + dx, c + dy
            r, c = nx, ny
        sharks[sid] = r, c, s, d, z
        arr[r][c].append(sid)
    for _r in range(n):
        for _c in range(m):
            if len(arr[_r][_c]) > 1:
                mz, msid = 0, 0
                for sid in arr[_r][_c]:
                    r, c, s, d, z = sharks[sid]
                    if mz < z:
                        mz = z
                        msid = sid
                for sid in arr[_r][_c]:
                    if msid == sid:
                        continue
                    del sharks[sid]
    # # 겹치는게 있는지 확인
    # for sid in range(1, k+1):
    #     if sharks.get(sid) is None:
    #         continue
    #     r, c, s, d, z = sharks[sid]
    #     for oth_sid in range(sid+1, k+1):
    #         if sharks.get(oth_sid) is None:
    #             continue
    #         _r, _c, _s, _d, _z = sharks[oth_sid]
    #         if [r, c] == [_r, _c]:
    #             if z > _z:
    #                 del sharks[oth_sid]
    #             else:
    #                 del sharks[sid]
    #                 break
    arr = [[[] for _ in range(m)] for _ in range(n)]
print(ans)