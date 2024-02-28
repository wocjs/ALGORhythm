#include <iostream>
#include <stack>
using namespace std;
int n, m;
int dx[8] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[8] = {0, 0, -1, 1, -1, 1, -1, 1};
int arr[51][51];
bool visited[51][51];


void dfs(int x, int y){
    for(int i=0;i<8;i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && arr[nx][ny]){
            visited[nx][ny] = 1;
            dfs(nx, ny);
        }
    }
}


int main(){
    while (true){
        cin >> m >> n;
        if(n == 0 && m == 0)break;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin >> arr[i][j];
            }
        }
        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(arr[i][j] && !visited[i][j]){
                    visited[i][j] = 1;
                    dfs(i, j);
                    ans++;
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                visited[i][j] = 0;
            }
        }
        cout << ans << endl;
    }
    return 0;
}