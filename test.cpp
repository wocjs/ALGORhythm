// B16946
#include <iostream>
#include <queue>

int n, m;
int arr[1000][1000];
int visited[1000][1000];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
using namespace std;

int bfs(int _x, int _y){
    queue<pair<int, int>> q;
    q.push(make_pair(_x, _y));
    visited[_x][_y] = 1;
    int cnt = 1;
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int i=0;i<4;i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0<=nx && nx<n && 0<=ny && ny<m && !visited[nx][ny] && !arr[nx][ny]){
                cnt++;
                visited[nx][ny]=1;
                q.push(make_pair(nx, ny));
            }
        }
    }
    return cnt;
}
void flush(){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            visited[i][j] = 0;
        }
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    string inp;
    for(int i=0;i<n;i++){
        cin >> inp;
        for(int j=0;j<inp.length();j++){
            arr[i][j] = inp[j] - '0';
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(arr[i][j] == 1){
                flush();
                arr[i][j] = bfs(i, j);
            }
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout << arr[i][j];
        }
        cout << "\n";
    }
    return 0;
}