#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(){
    // 1918
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string arr;
    stack<char> st;
    cin >> arr;

    for(int i = 0;i<arr.length();i++){
        // 큰따옴표는 문자열, 작은따옴표는 문자로 인식하여 연상니 가능해지니 주의
        if ('A' <= arr[i] && arr[i] <= 'Z'){
            cout << arr[i];
        }
        else{
            if (arr[i] == '('){
                st.push(arr[i]);
            }
            else if(arr[i] == '*' || arr[i] == '/'){
                while(!st.empty() && (st.top() == '*' || st.top() == '/')){
                    cout << st.top();
                    st.pop();
                }
                st.push(arr[i]);
            }
            else if(arr[i] == '+' || arr[i] == '-'){
                while(!st.empty() && st.top() != '('){
                    cout << st.top();
                    st.pop();
                }
                st.push(arr[i]);
            }
            else if(arr[i] == ')'){
                while(!st.empty() && st.top() != '('){
                    cout << st.top();
                    st.pop();
                }
                st.pop();
            }
        }
    }
    while (!st.empty()){
        cout << st.top();
        st.pop();
    }

    return 0;
}