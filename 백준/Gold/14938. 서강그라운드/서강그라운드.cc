#include <iostream>

using namespace std;
int INF = 1000000000;
int n, m, r;
int item[101];
int graph[101][101];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m >> r;
    for(int i=1;i<n+1;i++){
        cin >> item[i];
    }

    // Init
    for(int i=0;i<n+1;i++){
        for(int j=0;j<n+1;j++){
            graph[i][j] = INF;
        }
        graph[i][i] = 0;
    }
    int a, b, l;
    for(int i=0;i<r;i++){
        cin >> a >> b >> l;
        graph[a][b] = min(graph[a][b], l);
        graph[b][a] = min(graph[b][a], l);
    }
    
    // Floyd Warshall
    for(int k=1;k<n+1;k++){
        for(int i=1;i<n+1;i++){
            for(int j=0;j<n+1;j++){
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j]);
            }
        }
    }
    /*
    for(int i =0;i<n+1;i++){
        for(int j = 0;j<n+1;j++){
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
    */
    int ans = 0;
    for(int i=1;i<n+1;i++){
        int tmp = 0;
        for(int j = 0;j<n+1;j++){
            if (graph[i][j] <= m){
                tmp += item[j];
            }
        }
        ans = max(ans, tmp);
    }
    cout << ans << endl;
    return 0;
}
