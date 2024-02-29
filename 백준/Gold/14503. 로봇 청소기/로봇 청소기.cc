#include <iostream>
using namespace std;

int n, m;
int x, y, d;
int arr[50][50];
bool visited[50][50];
// 북, 동, 남, 서
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int cnt;

void dfs(){
    // 네 방향 청소, 계속 반시계 방향으로 회전
    for(int i=0;i<4;i++){
        // 반시계 : 북 - 서 - 남 - 동 = (now+3-i)%4
        int nd = (d+3-i) % 4;
        int nx = x + dx[nd];
        int ny = y + dy[nd];
        if(0 <= nx && nx < n && 0 <= ny && ny < m && !arr[nx][ny] && !visited[nx][ny]){
            visited[nx][ny] = 1;
            x = nx;
            y = ny;
            d = nd;
            cnt++;
            dfs();
        }
    }
    // 뒤로가기
    int bx = x - dx[d];
    int by = y - dy[d];
    if (0<= bx && bx < n && 0 <= by && by < m){
        if(arr[bx][by] == 0){
            x = bx;
            y = by;
            dfs();
        }
        else{
            cout << cnt << "\n";
            exit(0);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    cin >> x >> y >> d;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin >> arr[i][j];
        }
    }
    visited[x][y] = 1;
    cnt++;
    
    dfs();

    return 0;
}