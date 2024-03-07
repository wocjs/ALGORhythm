// B1427
#include <iostream>
#include <algorithm>

using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    string str;
    cin >> str;
    sort(str.begin(), str.end(), greater<char>());
    cout << str;

    return 0;
}