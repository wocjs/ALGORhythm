#include<iostream>
#include<string.h>
using namespace std;
int main(){
    // 9935
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string str;
    string bomb;
    string stack = "";
    cin >> str >> bomb;
    int n = str.length();
    int m = bomb.length();
    for(int i=0;i<n;i++){
        stack += str[i];
        if(stack.length() >= m){
            bool flag = true;
            for (int j=0;j<m;j++){
                if (stack[stack.length()-m+j] != bomb[j]){
                    flag = false;
                    break;
                }
            }
            if(flag){
                stack.erase(stack.end() - m, stack.end());
            }
        }
    }
    if(stack.empty())
        cout << "FRULA" << endl;
    else
        cout << stack << endl;
    return 0;
}