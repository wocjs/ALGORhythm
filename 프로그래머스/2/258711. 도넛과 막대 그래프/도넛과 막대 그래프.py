
def solution(edges):
    # 생성된 정점 : (진출차수 >= 2 & 진입차수 == 0)을 만족하는 노드
    # 막대모양 그래프 수 : (진출차수 == 0 & 진입차수 == 1)을 만족하는 노드의 수
    # 8자모양 그래프 수 : (진출차수 == 2 & 진입차수 == 2)을 만족하는 노드의 수
    # 도넛모양 그래프 수 : 생성된 정점의 진출차수 - 막대모양 그래프 수 - 8자모양 그래프 수
    indeg = [0] * 1000000
    outdeg = [0] * 1000000
    for edge in edges:
        fr, to = edge
        indeg[to] += 1
        outdeg[fr] += 1

    ans = [0, 0, 0, 0]  # 생성, 도넛, 막대, 8자
    for i in range(1000000):
        if indeg[i] == 0 and outdeg[i] >= 2:    # 생성된 정점
            ans[0] = i
        elif indeg[i] >= 1 and outdeg[i] == 0:  # 막대모양
            ans[2] += 1
        elif indeg[i] >= 2 and outdeg[i] == 2:  # 8자모양
            ans[3] += 1
    ans[1] = outdeg[ans[0]] - ans[2] - ans[3]   # 도넛모양
    return ans