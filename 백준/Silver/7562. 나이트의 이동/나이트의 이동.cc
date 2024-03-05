// B7526
#include <iostream>
#include <queue>
using namespace std;
int T, l;
int arr[301][301];
int visited[301][301];
int dx[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[8] = {-1, 1, -2, 2, -2, 2, -1, 1};
int stx, sty, enx, eny;
queue<pair<int, int>> q;


void refresh(int _l){
    for(int i=0;i<_l;i++){
        for(int j=0;j<_l;j++){
            arr[i][j] = 0;
            visited[i][j] = 0;
        }
    }
    while(!q.empty()){
        q.pop();
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> T;
    for(int tc=1;tc<T+1;tc++){
        cin >> l;
        cin >> stx >> sty;
        cin >> enx >> eny;
        q.push(make_pair(stx, sty));
        visited[stx][sty] = 1;
        while (!q.empty()){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            if(x == enx && y == eny){
                cout << visited[enx][eny]-1 << "\n";
                refresh(l);
                break;
            }
            for (int i=0;i<8;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0 <= nx && nx < l && 0 <= ny && ny < l && !visited[nx][ny]){
                    visited[nx][ny] = visited[x][y] + 1;
                    q.push(make_pair(nx,ny));
                }
            }
        }
    }
    return 0;
}