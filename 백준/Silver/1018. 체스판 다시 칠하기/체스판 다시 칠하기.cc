#include <iostream>

using namespace std;

char map[52][52];
char wb[8][8];
char bw[8][8];
int n, m;
int mn = 50 * 50;

void makeMap() {
    for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++) {
			if (i % 2 == 0 && j % 2 == 0)
            {
				wb[i][j] = 'W';
				bw[i][j] = 'B';
			}
			else if(i%2 == 1 && j%2 == 0)
            {
				wb[i][j] = 'B';
				bw[i][j] = 'W';
			}
            else if (i%2 == 0 && j%2 == 1)
            {
                wb[i][j] = 'B';
                bw[i][j] = 'W';
            }
            else
            {
                wb[i][j] = 'W';
				bw[i][j] = 'B';
            }
        }
	}
}

int main() {
    makeMap();
    scanf("%d", &n);
    scanf("%d", &m);
    for (int i = 0; i < n; i++) { // 전체 지도 입력 받기
        getchar();
        for (int j = 0; j < m; j++) {
            scanf("%c", &map[i][j]);
        }
    }
    // for (int i = 0; i < 8; i++)
    // {
    //     for (int j = 0; j < 8; j++)
    //     {
    //         printf("%c", wb[i][j]);
    //     }
    //     printf("\n");
    // }
    // printf("\n\n");
    for (int i = 0; i <= n - 8; i++) {
        for (int j = 0; j <= m - 8; j++) {
            int BWcnt = 0, WBcnt = 0;
            for (int x = 0; x < 8; x++) {
                for (int y = 0; y < 8; y++) {
                    if (map[i + x][j + y] != wb[x][y]) {
                        WBcnt++;
                    }
                    if (map[i + x][j + y] != bw[x][y]) {
                        BWcnt++;
                    }
                }
            }
            mn = min(mn, min(WBcnt, BWcnt)); // 최솟값 갱신
        }
        // printf("%d, %d\n", i+8, j+8);
    }
    
    printf("%d\n", mn);
    return 0;
}
