//통과는 했는데 좀 더럽게 풀었음
#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;
#define INF 2147483647
#define MAX 50001
#define MAX_DEPTH 17

int V, E, u, v, w;
vector<tuple<int, int, int>> adj;
vector<vector<pair<int, int>>> mst;
int parent[MAX], depth[MAX];
int mstParent[MAX][MAX_DEPTH];
int maxWeight[MAX][MAX_DEPTH];
int secondMaxWeight[MAX][MAX_DEPTH];
int mstWeight, mstEdgeCnt;

int kruskal();
int find(int a);
bool uni(int a, int b);
int addEdge(int i);
void makeTree(int cur, int par);
int findLSA(int u, int v);
pair<int, int> getWeightOnPath(int u, int v);
pair<int, int> getWeights(pair<int, int> a, pair<int, int> b);

int main(){
    scanf("%d%d", &V, &E);
    for (int i = 0; i < E; i++){
        scanf("%d%d%d", &u, &v, &w);
        adj.push_back({w, u, v}); 
    }

    for (int i = 1; i <= V; i++) parent[i] = i;
     //MST를 만들어 봄
    
    mst.resize(V + 1);
    mstWeight = kruskal();
    if (mstEdgeCnt != V - 1) {
        printf("-1");
        return 0;
    }

    //트리로 만들고 모든 간선들을 보면서 추가해 보자(200,000)
    makeTree(1, 0);
    for (int j = 1; j < MAX_DEPTH; j++) {
        for (int i = 0; i <= V; i++){
            if (mstParent[i][j-1]) {
                mstParent[i][j] = mstParent[mstParent[i][j-1]][j-1];
                maxWeight[i][j] = max(maxWeight[i][j-1], maxWeight[mstParent[i][j-1]][j-1]);
                if (maxWeight[i][j-1] != maxWeight[mstParent[i][j-1]][j-1]) secondMaxWeight[i][j] = min(maxWeight[i][j-1], maxWeight[mstParent[i][j-1]][j-1]);
                else secondMaxWeight[i][j] = max(secondMaxWeight[i][j-1], secondMaxWeight[mstParent[i][j-1]][j-1]);
            }
        }
    }

    int secondMstWeight = INF;
    for (int i = 0; i < E; i++) {
        int addedWeight = addEdge(i);
        if (addedWeight < secondMstWeight && addedWeight > mstWeight) secondMstWeight = addedWeight; 
    }
    
    //바뀐 게 없으면 second mst가 존재하지 않는다는 것.
    if (secondMstWeight == INF) printf("-1");
    else printf("%d", secondMstWeight);
}

int kruskal(){
    int weight = 0;//mst의 가중치
    sort(adj.begin(), adj.end());//가중치 크기대로 일단 정렬
    for (auto edge : adj){
        int w = get<0>(edge), u = get<1>(edge), v = get<2>(edge);
        if (uni(u, v)) {
            //printf("mst: %d-%d(%d)\n", u, v, w);    
            weight += get<0>(edge);
            mst[u].push_back({v, w});
            mst[v].push_back({u, w});
            mstEdgeCnt++;
        }
    }
    return weight;
}

int find(int a){
    if (parent[a] == a) return a;
    return parent[a] = find(parent[a]);
}

bool uni(int a, int b){
    a = find(a);
    b = find(b);
    if (a == b) return false;
    if (a > b) swap(a, b);
    parent[b] = a;
    return true;
}

int addEdge(int i){
    auto edge = adj.at(i);
    int w = get<0>(edge), u = get<1>(edge), v = get<2>(edge);
    if ((mstParent[u][0] == v && maxWeight[u][0] == w) || (mstParent[v][0] == u && maxWeight[v][0] == w)) return mstWeight; //이미 mst에 존재하는 간선인 경우는 제외하기 
    //u -> v로 가는 경로에서의 최대 가중치를 찾고 그걸 빼고 내 가중치를 넣으면 됨.
    int LSA= findLSA(u, v);
    pair<int, int> weightOnPathUL = getWeightOnPath(u, LSA);
    pair<int, int> weightOnPathVL = getWeightOnPath(v, LSA);
    pair<int, int> weights = getWeights(weightOnPathUL, weightOnPathVL);
    int weightOnPath = weights.first == w ? weights.second : weights.first; 

    //printf("delete %d and add %d\n", weightOnPath, w);
    return mstWeight - weightOnPath + w;
}

void makeTree(int cur, int par){
    for (pair<int, int> child : mst[cur]){
        if (child.first != par){
            depth[child.first] = depth[cur] + 1;
            mstParent[child.first][0] = cur;
            maxWeight[child.first][0] = child.second;
            secondMaxWeight[child.first][0] = child.second;
            makeTree(child.first, cur);
        }
    }
}

int findLSA(int a, int b){
    int u = a, v = b;
    if (depth[u] < depth[v]) swap(u, v);
    int diff = depth[u] - depth[v];
    int ret = 0;
    while (diff){
        int d = 0;
        for (int i = 1; i <= diff; i *= 2) d++;
        u = mstParent[u][d-1];
        diff = depth[u] - depth[v];
    }

    if (u != v){
        for (int j = MAX_DEPTH - 1; j>= 0; j--){
            if (mstParent[u][j] && mstParent[u][j] != mstParent[v][j]) {
                u = mstParent[u][j];
                v = mstParent[v][j];
            }
        }

        u = mstParent[u][0];
    }
    //printf("maxWeight_%d-%d: %d, maxWeight_%d-%d: %d\n", a, anc, maxWeight_u, b, anc, maxWeight_v);
    return u;
}

pair<int, int> getWeightOnPath(int u, int anc){
    int diff = depth[u] - depth[anc];
    int maxWeightOnPath = -1, secondWeightOnPath = -1;
    int idx = 0;

    while (diff){
        if(diff & (1 << idx)) {
            maxWeightOnPath = max(maxWeightOnPath, maxWeight[u][idx]);
            secondWeightOnPath = (maxWeightOnPath == maxWeight[u][idx] ? max(secondWeightOnPath, secondMaxWeight[u][idx]) : min(maxWeightOnPath, maxWeight[u][idx])); 
            u = mstParent[u][idx];                
        }
        diff &= ~(1 << idx++);
    }
    return {maxWeightOnPath, secondWeightOnPath};
}

pair<int, int> getWeights(pair<int, int> a, pair<int, int> b){
    int arr[4] = {a.first, a.second, b.first, b.second};
    sort(arr, arr+4);
    int first = arr[3];
    int second = -1;
    for (int i = 2; i >= 0; i--){
        if (arr[i] == first) continue;
        second = arr[i];
        break;
    }
    if (second == -1) second = first;
    return {first, second};
}