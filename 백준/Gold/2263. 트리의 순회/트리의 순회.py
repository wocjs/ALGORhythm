import sys
sys.setrecursionlimit(10**6)


def find(ins, ine, pos, poe):  # 중위 시/끝, 후위 시/끝
    if ins > ine or pos > poe:
        return

    root = postorder[poe]
    print(root, end=' ')

    lenleft = nodeNum[root] - ins   # 중위 시작 ~ 루트 위치 인덱스
    lenright = ine - nodeNum[root]  # 루트 인덱스 ~ 중위 끝

    # 중위시작, 중위시작+왼길이-1, 후위시작, 후위시작+왼길이-1
    find(ins, ins+lenleft-1, pos, pos+lenleft-1)
    # 중위끝-오길이+1, 중위끝, 후위끝-오길이+1, 후위끝-1(후위 끝은 root였음)
    find(ine-lenright+1, ine, poe-lenright, poe-1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 후위순회의 값이 중위순회의 어디 인덱스에 위치한지 기록
# inorder = index, inorder의 인덱스 == value
nodeNum = [0] * (n + 1)
for i in range(n):
    nodeNum[inorder[i]] = i
find(0, n-1, 0, n-1)
