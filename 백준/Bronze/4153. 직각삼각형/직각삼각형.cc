#include <iostream>

using namespace std;


void check(int mx, int a, int b){
    if (mx * mx == (a * a + b * b)){
        cout << "right\n";
    }
    else
        cout << "wrong\n";
}


int main() {
    while(true)
    {
        int x, y, z;
        int tmp = 0;
        scanf("%d %d %d", &x, &y, &z);
        if (x + y + z == 0){
            break;
        }
        if (max(x, max(y, z)) == x){
            check(x, y, z);
        }
        else if (max(y, max(x, z)) == y){
            check(y, x, z);
        }
        else{
            check(z, x, y);
        }
    }
    return 0;
}
