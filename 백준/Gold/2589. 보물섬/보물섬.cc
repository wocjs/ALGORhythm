// B1427
#include <iostream>
#include <queue>

int n, m;
char arr[50][50];
int visited[50][50];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

using namespace std;
void flush(){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            visited[i][j] = 0;
        }
    }
}
int bfs(int a, int b){
    queue<pair<int, int>> q;
    q.push(make_pair(a, b));
    visited[a][b] = 1;
    int mx=0;
    while (!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int d=0;d<4;d++){
            int nx = x + dx[d];
            int ny = y + dy[d];
            if(0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && arr[nx][ny] == 'L'){
                q.push(make_pair(nx, ny));
                visited[nx][ny] = visited[x][y] + 1;
                mx = max(visited[nx][ny], mx);
            }
        }
    }
    return mx;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            cin >> arr[i][j];
        }
    }
    int ans = 0;
    for (int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(arr[i][j] == 'L'){
                flush();
                ans = max(ans, bfs(i, j));
            }
        }
    }
    cout << ans-1 << "\n";
    return 0;
}