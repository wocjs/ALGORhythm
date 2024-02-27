#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int n, cnt;
int ans = 0;
int mxnum = 0;
bool visited[101][101];
int arr[101][101];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
queue<pair<int, int>> q;

int main(){
    // 입력
    cin >> n;
    for (int i = 0;i<n;i++){
        for(int j = 0;j<n;j++){
            cin >> arr[i][j];
            mxnum = max(mxnum, arr[i][j]);
            visited[i][j] = false;
        }
    }
    // 높이 1부터 맥스까지
    for(int height=0;height<mxnum;height++){
        cnt = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if (arr[i][j] > height && !visited[i][j]){
                    //bfs
                    q.push(make_pair(i, j));
                    visited[i][j] = true;
                    while(!q.empty()){
                        int x = q.front().first;
                        int y = q.front().second;
                        q.pop();
                        for(int d=0;d<4;d++){
                            int nx = x + dx[d];
                            int ny = y + dy[d];
                            if (0 <= nx && nx < n && 0 <= ny && ny < n && arr[nx][ny] > height && !visited[nx][ny]){
                                visited[nx][ny] = true;
                                q.push(make_pair(nx, ny));
                            }
                        }
                    }
                    cnt++;
                }
            }
        }
        ans = max(cnt, ans);
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                visited[i][j] = 0;
            }
        }
    }
    cout << ans << endl;
    return 0;
}