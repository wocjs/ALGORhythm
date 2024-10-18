
import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root
        for food in foods:
            if food not in cur:
                cur[food] = {}  # 자식 노드
            cur = cur[food]
        cur[0] = True  # 리프 노드 표시

    def travel(self, level, cur):
        if 0 in cur:
            return
        cur_child = sorted(cur)

        for ch in cur_child:
            print("--" * level, end='')
            print(ch)
            self.travel(level + 1, cur[ch])


N = int(input())
trie = Trie()
for i in range(N):
    data = list(input().split())
    trie.add(data[1:])
trie.travel(0, trie.root)
